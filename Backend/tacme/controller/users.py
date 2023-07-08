from flask import Blueprint, request
from tacme.model.login_request import LoginRequest
from tacme.service.user import attempt_login
users = Blueprint('users', __name__, url_prefix='/users')

@users.route('/login', methods=['POST'])
def login():
    req = LoginRequest(request.form.get('username'), request.form.get('password'))
    res = attempt_login(req)
    if res == '':
        return "sorry chum", 401
    return res

