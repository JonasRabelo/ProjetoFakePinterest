from flask import Flask
from flask_sqlalchemy import SQLAlchemy #pip install flask_sqlalchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"
database = SQLAlchemy(app)

from ProjetoFakePinterest import routes

