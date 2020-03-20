from flask_mail import Mail

mail = Mail()
config = {
    "SERVER": "",
    "PORT": 587,
    "USE_TLS": True,
    "USERNAME": "",
    "DEFAULT_SENDER": "",
    "PASSWORD": "",
}
