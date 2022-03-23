from flask import *
import jwt
from os import path
from functools import wraps


def load_key(keys_dir, kid):
    if not kid or not path.exists(path.join(keys_dir, kid)):
        return None    

    with open(path.join(keys_dir, kid)) as key_file:
        key = key_file.read()
    return key


def token_required():
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = request.headers.get('Authorization')

            if not token:
                return make_response('Token Required', 401)
            
            try:
                headers = jwt.get_unverified_header(token)
            except:
                return make_response('Invalid Token', 401)
            
            kid = headers.get("kid")
            secret_key = load_key(kid)

            if secret_key is None:
                return make_response('Invalid Token', 401)

            # Verify token is valid
            try:
                data = jwt.decode(token, secret_key, algorithms=['HS256'])
            except:
                return make_response('Invalid Token', 401)

            return f(*args, **kwargs)
        return decorated

    return decorator
