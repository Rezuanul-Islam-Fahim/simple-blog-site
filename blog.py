from flask import (
    Blueprint, g, request, url_for, render_template, redirect, flash
)
from werkzeug.exceptions import abort

from database import get_db
from auth import login_required

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


def get_post(id):
    post = get_db().execute(
        'SELECT title, body, author_id FROM post WHERE id = ?', [id]
    ).fetchone()

    if g.user is None:
        abort(403)
    elif post is None:
        abort(404, 'Post with id:{} doesn\'t exists'.format(id))
    elif g.user['id'] != post['author_id']:
        abort(401, 'You are not authorized to access the URL requested.')
    else:
        return post


@bp.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None
        db = get_db()

        if not title:
            error = 'Title is required'
        elif not body:
            error = 'Body is required'
        else:
            db.execute(
                'UPDATE post SET title = ?, body = ? WHERE id = ?',
                [title, body, id]
            )
            db.commit()

            return redirect(url_for('blog.index'))

        if (error): flash(error)

    return render_template('blog/update.html', post=post)


@bp.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', [id])
    db.commit()
    return redirect(url_for('blog.index'))
