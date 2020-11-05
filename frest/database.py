from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
config = {"DATABASE_URI": "sqlite:///database.db"}
