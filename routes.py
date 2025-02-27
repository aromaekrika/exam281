from flask import Blueprint, render_template

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return render_template('index.html')

@routes.route('/about')
def about():
    return "This is the About page!"
