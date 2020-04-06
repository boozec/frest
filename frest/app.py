from flask import Flask
from auth.routes import api as api_users
from flask import make_response, jsonify
from database import db
from database import config as db_config
from mail import mail
from mail import config as mail_config
from flask_sqlalchemy import SQLAlchemy
from utils import http_call
from flask_cors import CORS
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = db_config["DATABASE_URI"]
app.config["DEBUG"] = os.getenv("FREST_DEBUG", True)
app.config["CORS_HEADERS"] = "Content-Type"
app.config["MAIL_SERVER"] = mail_config["SERVER"]
app.config["MAIL_PORT"] = mail_config["PORT"]
app.config["MAIL_USE_TLS"] = mail_config["USE_TLS"]
app.config["MAIL_USERNAME"] = mail_config["USERNAME"]
app.config["MAIL_DEFAULT_SENDER"] = mail_config["DEFAULT_SENDER"]
app.config["MAIL_PASSWORD"] = mail_config["PASSWORD"]

cors = CORS(app, resources={r"/.*": {"origins": "*"}})
db.app = app
db.init_app(app)
mail.init_app(app)
app.register_blueprint(api_users)


@app.errorhandler(404)
def not_found(error):
    return http_call("Not found", 404)


@app.errorhandler(400)
def bad_request(error):
    return http_call("Bad request", 400)


@app.errorhandler(405)
def method_not_allowed(error):
    return http_call("Method not allowed", 405)


@app.errorhandler(403)
def forbiddend(error):
    return http_call("Forbidden", 403)


@app.errorhandler(500)
def internal(error):
    return http_call("Internal error", 500)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
