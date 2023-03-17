from . import db

class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200))
    is_done = db.Column(db.Boolean)
    date = db.Column(db.DateTime(timezone=True))