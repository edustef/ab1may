from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b29a5e61816e3c104500566e4909327d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db =  SQLAlchemy(app)

from application import routes