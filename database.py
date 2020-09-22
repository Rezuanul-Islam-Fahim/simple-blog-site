import sqlite3
import click
from flask import g, current_app
from flask.cli import with_appcontext


def get_db():
    """ Function for opening database and return it
    to a variable for using it anywhere """

    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES,
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    """ Close db after every app-context ends """

    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    """ Initialize database and execute sql schema's for
    creating user and post table """

    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """ Add initialize db function to flask cli """

    init_db()
    click.echo('Database initialized')


def init_app(app):
    """ Function for registering init-db function to flask app """

    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
