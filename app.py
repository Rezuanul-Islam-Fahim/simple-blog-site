import os
from flask import Flask

import database
import auth
import blog


app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='DEV',
    DATABASE=os.path.join(app.instance_path, 'data.sqlite'),
)

try:
    os.makedirs(app.instance_path)
except OSError:
    pass

database.init_app(app)

app.register_blueprint(auth.bp)

app.register_blueprint(blog.bp)
app.add_url_rule('/', 'index')
