from database import db
from datetime import datetime
import string
import random
from hashlib import sha256
from pytz import timezone
import os


def generate_token():
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return "".join(random.choice(chars) for _ in range(18))


class User(db.Model):
    userId = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30))
    password = db.Column(db.String(30))
    is_admin = db.Column(db.Boolean, default=False)
    name = db.Column(db.String(30))
    created_at = db.Column(db.DateTime)

    def __init__(self, **kwargs):
        self.email = kwargs.get("email")
        psw_hash = sha256(kwargs.get("password").encode())
        self.password = psw_hash.hexdigest()
        self.name = kwargs.get("name")
        self.is_admin = kwargs.get("is_admin")
        self.created_at = datetime.now(
            timezone(os.getenv("FREST_TIMEZONE", "Europe/Rome"))
        )

    def __repr__(self):
        return f"<User '{self.userId}'>"


class Token(db.Model):
    tokenId = db.Column(db.Integer, primary_key=True)
    string = db.Column(db.String(20))
    created_at = db.Column(db.DateTime)
    expired = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey("user.userId"), nullable=False)
    user = db.relationship("User", backref=db.backref("tokens", lazy=True))

    def __init__(self, user):
        self.user = user
        self.string = f"{generate_token()}=="
        self.created_at = datetime.utcnow()
        self.expired = False

        def __repr__(self):
            return f"<Token '{self.string}'>"
