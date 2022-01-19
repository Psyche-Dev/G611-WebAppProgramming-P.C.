from flask_login import login_required,current_user
from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def forum():
    return render_template("forum.html")

@views.route('/news')
def news():
    return render_template("news.html")