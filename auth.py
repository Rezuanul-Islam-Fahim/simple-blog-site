import functools
from flask import (
    Blueprint, g, flash, redirect, session, request, url_for, render_template
)
from werkzeug.security import generate_password_hash, check_password_hash

from database import get_db

# User authentication blueprint
bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    """ View function for handling user registration """

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required'
        elif not password:
            error = 'Password is required'
        elif db.execute(
              'SELECT id FROM user WHERE username = ?', [username]
        ).fetchone() is not None:
            error = 'User {} is already registered'.format(username)

        if error is None:
            db.execute(
                'INSERT INTO user (username, password) '
                'VALUES (?, ?)', [username, generate_password_hash(password)]
            )
            db.commit()

            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    """ View function for handling user login """

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        user = db.execute(
            'SELECT id, password FROM user WHERE username = ?', [username]
        ).fetchone()
        error = None

        if not username:
            error = 'Username is required'
        elif not password:
            error = 'Password is required'
        elif user is None:
            error = 'User {} is not registered'.format(username)
        elif not check_password_hash(user['password'], password):
            error = 'Password doesn\'t match'

        if error:
            flash(error)
        else:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

    return render_template('auth/login.html')


@bp.before_app_request
def load_logged_in_user():
    """ This function will load logged in user to every context
    and will load automatically before every context call,
    even if it is outside of auth blueprint """

    user_id = session.get('user_id')

    if user_id is not None:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', [user_id]
        ).fetchone()
    else:
        g.user = None


@bp.route('/logout')
def logout():
    """ Function for logging out user and redirect to homepage """

    session.clear()
    return redirect(url_for('index'))


def login_required(view):
    """ This function will check if a user is logged in or not.
    If not then it will redirect user to login view """

    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
