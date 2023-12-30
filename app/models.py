from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Language(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    code = db.Column(db.String(10), nullable=False, unique=True)
    audio_file = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self):
        return f"Language('{self.name}', '{self.code}', '{self.audio_file}')"
