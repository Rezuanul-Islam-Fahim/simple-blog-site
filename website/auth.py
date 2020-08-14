from flask import (
    Blueprint, g, flash, redirect, session
)

bp = Blueprint('auth', __name__, url_prefix='/auth')