from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

class Level(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    subjects = db.relationship('Subject', backref='level', lazy=True)

    def __init__(self, name):
        self.name = name

class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True,nullable=False)
    level_id = db.Column(db.Integer, db.ForeignKey(level.id),
    nullable=False)


@app.route('/')
def hello():
    return "Hello Cyberpeaks!"

if __name__ == '__main__':
    app.run()
