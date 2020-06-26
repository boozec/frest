from flask import Blueprint, request, abort
from frest.utils import http_call, model_serialize
from frest.decorators import check_token, admin_required
from .models import User, Token
from .forms import UserForm
from database import db
from hashlib import sha256
from sqlalchemy import desc

api = Blueprint("users", __name__)


@api.route("/api/login", methods=["POST"])
def login():
    if not request.json:
        abort(400)

    data = request.json

    auth = request.headers.get("Authorization")
    if auth:
        t = Token.query.filter_by(string=auth).first()
        if not t:
            abort(404)

        if t.user.is_admin:
            return http_call(
                {"userId": t.user.userId, "login": True, "token": t.string}, 200
            )
        else:
            abort(403)

    if "email" in data and "password" in data:
        psw_hash = sha256(data["password"].encode())
        data["password"] = psw_hash.hexdigest()
        u = User.query.filter_by(email=data["email"], password=data["password"]).first()

        if not u:
            abort(404)

        if "is_admin" in data:
            if u.is_admin == 0:
                abort(403)

        last_token = (
            Token.query.filter_by(user=u).order_by(desc(Token.tokenId)).all()[-1]
        )
        last_token.expired = True

        t = Token(user=u)

        db.session.add(t)
        db.session.commit()

        return http_call({"userId": u.userId, "login": True, "token": t.string}, 200)

    abort(404)


@api.route("/api/user/hash_password", methods=["GET"])
def hash_password_exists():
    data = request.args
    if not data.get("hash_password"):
        abort(400)

    if User.query.filter_by(password=data["hash_password"]):
        return http_call({}, 200)

    return http_call({}, 404)


@api.route("/api/user/new-password/<alias>", methods=["PUT"])
def new_user_password(alias):
    data = request.json
    if not data.get("password"):
        abort(400)

    u = User.query.filter_by(password=alias).first()

    if not u:
        abort(404)

    u.password = sha256(data["password"].encode()).hexdigest()
    db.session.commit()

    return http_call({}, 200)


@api.route("/api/user", methods=["POST"])
def new_user():
    if not request.json:
        abort(400)

    form = UserForm(request.json)

    if not form.get("is_admin") or form.is_valid():
        if User.query.filter_by(email=form.get("email")).first():
            abort(400)

        u = User(
            email=form.get("email"),
            password=form.get("password"),
            name=form.get("name"),
            is_admin=False,
        )
        t = Token(user=u)
        db.session.add(u)
        db.session.add(t)

        db.session.commit()

        return http_call({"userId": u.userId, "token": t.string}, 201)

    abort(400)


@api.route("/api/users")
@check_token
@admin_required
def all_users():
    return http_call(
        [
            model_serialize(i, params="userId,email,is_admin,name,created_at")
            for i in User.query.all()
        ],
        200,
    )


@api.route("/api/user/<int:userId>")
@check_token
def get_user(userId):
    return http_call(
        model_serialize(
            User.query.filter_by(userId=userId).first(),
            params="userId,email,is_admin,name,created_at",
        ),
        200,
    )


@api.route("/api/user/<userId>", methods=["DELETE"])
@check_token
def delete_user(userId):
    u = User.query.filter_by(userId=userId)
    if not u:
        abort(404)

    deleted = u.delete()
    db.session.commit()

    return http_call({"delete": deleted}, 200)


@api.route("/api/user/<userId>", methods=["PUT"])
@check_token
def edit_user(userId):
    if not request.json:
        abort(400)

    form = UserForm(request.json)
    u = User.query.filter_by(userId=userId).first()
    if not u:
        abort(400)

    if form.get("password"):
        psw = True
    else:
        psw = False

    if not psw or not form.get("is_admin") or form.is_valid():
        u.name = form.get("name")
        u.email = form.get("email")
        u.is_admin = form.get("is_admin")
        if psw:
            crypt_psw = sha256(form.get("password").encode()).hexdigest()
            u.password = crypt_psw

        db.session.commit()

        return http_call({"userId": u.userId}, 200)

    abort(400)
