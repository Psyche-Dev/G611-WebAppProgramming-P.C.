from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("forum.html")

@views.route('/news')
def news():
    return render_template("news.html")