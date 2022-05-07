from flask import Flask




app = Flask(__name__)


from os import environ


app.config['SECRET_KEY']= environ.get('SECRET_KEY')




from portfolio import views

from .views import views


app.register_blueprint (views, url_prefix ="/")



