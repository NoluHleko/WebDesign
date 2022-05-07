
from flask import Blueprint, Flask, render_template
from portfolio import app


views = Blueprint("views",__name__)




 #home page view
@views.route('/')
@views.route('/home')
def home():
    return render_template('portfolio.html')


