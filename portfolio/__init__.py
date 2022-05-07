from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)


from os import environ

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Weblog2022.db'
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')

app.config['SECRET_KEY']= environ.get('SECRET_KEY')
db = SQLAlchemy(app)



from portfolio import views

from .views import views


app.register_blueprint (views, url_prefix ="/")



