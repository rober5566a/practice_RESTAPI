# from application import db
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
app = Flask(__name__)
app.config['SQLALchemy_db_url'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Colunm(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"


@app.route('/')
def index():
    return "Hello"


@app.route('/drinks')
def get_drinks():
    return {'drink': "drink data"}
