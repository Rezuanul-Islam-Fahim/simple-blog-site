import os
from flask import Flask

import database
import auth
import blog

# Create flask app
app = Flask(__name__, instance_relative_config=True)

# App config
app.config.from_mapping(
    SECRET_KEY='DEV',
    DATABASE=os.path.join(app.instance_path, 'data.sqlite'),
)

# Create instance path
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

# Initialize database cli to app
database.init_app(app)

# Register auth blueprint to app
app.register_blueprint(auth.bp)

# Register blog blueprint to app
app.register_blueprint(blog.bp)

# Add root url rule
app.add_url_rule('/', 'index')
