from database import db
from datetime import datetime
from pytz import timezone
import os


class %%NAME%%(db.Model):
    %%name%%Id = db.Column(db.Integer, primary_key=True)
    %%params_model%%
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __init__(self, **kwargs):
        %%params_model_init%%
        self.created_at = datetime.now(
            timezone(os.getenv("FREST_TIMEZONE", "Europe/Rome"))
        )
        self.updated_at = datetime.now(
            timezone(os.getenv("FREST_TIMEZONE", "Europe/Rome"))
        )

    def __repr__(self):
        return f"<%%NAME%% '{self.%%name%%Id}'>"

    def __str__(self):
        return f"{self.%%name%%Id}"
