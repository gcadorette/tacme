from flask import Blueprint, request
from tacme.service.meme import get_all_memes, add_meme
from tacme.service.session import is_valid
from tacme.model.add_file_request import AddFileRequest
from tacme.model.exceptions import UNAUTHORIZED_EXCEPTION, SERVER_ERROR
memes = Blueprint('memes', __name__, url_prefix='/memes')

@memes.route('/', methods=['GET'])
def get_memes():
    memes = get_all_memes()
    return memes

@memes.route('/', methods=['POST'])
def post_meme():
    meme_request = AddFileRequest(request.form.get("user_hash"), request.form.get("meme"))
    is_session_valid = is_valid(meme_request.user_hash)
    if not is_session_valid:
        return UNAUTHORIZED_EXCEPTION
    else:
        inserted_id = add_meme(meme_request.meme)
        if inserted_id is None:
            return SERVER_ERROR
        return inserted_id


@memes.route('/allo', methods=['GET'])
def allo():
    return 'allo'