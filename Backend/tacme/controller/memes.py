from flask import Blueprint
from tacme.service.meme import get_all_memes
memes = Blueprint('memes', __name__, url_prefix='/memes')

@memes.route('/', methods=['GET'])
def get_memes():
    memes = get_all_memes()
    return memes

@memes.route('/', methods=['POST'])
def add_meme():
    return 'WIP:), manque auth tbh'

@memes.route('/allo', methods=['GET'])
def allo():
    return 'allo'