import os
from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='DEV',
        DATABASE=os.path.join(app.instance_path, 'data.sqlite')
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/test')
    def test():
        return 'This is just a test'

    import database
    database.init_app(app)

    import auth
    app.register_blueprint(auth.bp)

    import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', 'index')

    return app
