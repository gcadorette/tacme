from tacme.model.login_request import LoginRequest
from tacme.service.crypto import generate_hash
from tacme.client.mongo import get_users_collection
from tacme.service.session import create_session

def attempt_login(login_request: LoginRequest):
    user = get_users_collection().find_one({'username': login_request.username})
    if user == None:
        return ''
    salted_password = f'{user["salt"]}{login_request.password}'
    login_hash = generate_hash(salted_password)
    if login_hash == user['hash']:
        return create_session()
    return ''