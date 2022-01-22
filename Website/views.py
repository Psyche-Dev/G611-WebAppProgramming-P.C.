from flask_login import login_required,current_user
from flask import Blueprint, flash, render_template, request
from .models import Forumpost
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def forum():
    if request.method == 'POST':
        post = request.form.get('forumpost')

        if len(post) < 5:
            flash('Forum post must be greater than 5 chanracters', category='error')
        else:
            newreply = Forumpost(data=post, user_id = current_user.id)
            db.session.add(newreply)
            db.session.commit()
            flash('Reply created', category='success')

    return render_template("forum.html")

@views.route('/news')
def news():
    return render_template("news.html")

