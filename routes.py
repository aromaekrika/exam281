from flask import Blueprint, render_template

routes = Blueprint('routes', __name__)

@routes.route('/')
def home(): # route for the home page
    return render_template('index.html')

@routes.route('/about')
def about():
    return "This is the About page!"
