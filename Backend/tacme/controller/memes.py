from flask import current_app, Blueprint
memes = Blueprint('memes', __name__, url_prefix='/memes')

memes.route('/')
def index():
    return 'Allaw'