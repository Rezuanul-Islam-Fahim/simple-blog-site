from flask import (
    Blueprint, g, request, url_for, render_template, redirect, flash
)

from .database import get_db
from .auth import login_required

bp = Blueprint('blog', __name__)


@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        db = get_db()
        error = None

        if not title:
            error = 'Title is required'
        elif not body:
            error = 'Body is required'

        if error is None:
            db.execute(
                'INSERT INTO post (title, body, author_id) VALUES (?, ?, ?)',
                [title, body, g.user['id']]
            )
            db.commit()

            return redirect(url_for('blog.index'))

        flash(error)

    return render_template('blog/create.html')


@bp.route('/')
def index():
    posts = get_db().execute(
        'SELECT p.id, title, body, created, author_id, username FROM post p '
        'JOIN user u ON author_id = u.id ORDER by created DESC'
    ).fetchall()

    return render_template('blog/index.html', posts=posts)
