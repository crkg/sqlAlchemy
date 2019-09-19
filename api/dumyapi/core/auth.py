from flask import request
from base64 import b64decode
from functools import wraps


def authorize(f):
    @wraps(f)
    def inner(*args, **kwargs):
        if 'authorization' in request.headers:
            auth = request.headers.get('authorization').split()[1]
            username, password = b64decode(auth).decode('UTF-8').split(':')
            if username != 'Admin':
                return {'message': 'User not Authorized'}, 401
            if password != 'Sungard01':
                return {'message': 'Incorrect Password'}, 401
            return f(*args, **kwargs)
        else:
            return {'message': 'No credentials provide'}, 401
    return inner
