from flask import request, abort
from frest.auth.models import Token
from functools import wraps


def check_token(f):
    @wraps(f)
    def inner(*args, **kwargs):
        userid = request.url.split("/")[-1]
        headers = request.headers
        if not headers.get("Authorization"):
            abort(403)

        auth = headers.get("Authorization")
        token = Token.query.filter_by(string=auth).first()
        if not token:
            abort(403)

        if userid.isdigit():
            if int(userid) != token.user.userId and not token.user.is_admin:
                abort(403)

        return f(*args, **kwargs)

    return inner


def admin_required(f):
    @wraps(f)
    def inner(*args, **kwargs):
        auth = request.headers.get("Authorization")
        token = Token.query.filter_by(string=auth).first()
        if not token.user.is_admin:
            abort(403)

        return f(*args, **kwargs)

    return inner
