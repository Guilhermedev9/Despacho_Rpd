from flask import Blueprint, render_template # type: ignore

home_route = Blueprint('home', __name__)

#rota
@home_route.route('/')
def home():
    return render_template('index.html')