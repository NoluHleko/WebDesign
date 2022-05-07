
from flask import Blueprint, Flask, render_template
from portfolio import app


views = Blueprint("views",__name__)




 #home page view
@views.route('/')
@views.route('/home')
@views.route('/portfolio')
def home():
    return render_template('portfolio.html')


@views.route('/workflow')
def workflow():
    return render_template('workflow.html')

@views.route('/gallery-workflow')
def galleryworkflow():
    return render_template('gallery-workflow.html')

@views.route('/std-grid')
def StdGrid():
    return render_template('standard-grid.html')


