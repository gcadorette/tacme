from tacme.model.login_request import LoginRequest
from tacme.model.user import User
from tacme.model.file_format import FileFormat
from tacme.model.meme import Meme
from tacme.client.mongo import get_user_collection
import hashlib

def attempt_login(login_request: LoginRequest):
    user = get_user_collection().find_one({'username': login_request.username})
    if user == None:
        return ''
    salted_password = f'{user["salt"]}{login_request.password}'
    hashgen = hashlib.sha512()
    hashgen.update(str.encode(salted_password))
    login_hash = hashgen.hexdigest()
    if login_hash == user['hash']:
        # take care of session here :)
        return 'sessionId'
    return ''