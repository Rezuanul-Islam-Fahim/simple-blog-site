from flask import (
    Blueprint, g, request, url_for, render_template
)

from .database import get_db


bp = Blueprint('blog', __name__)


@bp.route('/')
def index():
    return 'Hello world'
