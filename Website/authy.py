from flask import Blueprint, Flask, render_template, request, redirect,url_for,flash
from .models import User
from werkzeug.security import generate_password_hash,check_password_hash
from . import db
from flask_login import login_user,login_required,logout_user,current_user

authy = Blueprint('authy', __name__)

@authy.route('/signin', methods=['GET','POST'])
def signin():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.Query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Signed In Succesfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect Password!', category='error')
        else:
            flash('Email does not exist', category='error')        

    return render_template("signin.html")

@authy.route('/signout')
@login_required
def signout():
    logout_user()
    return redirect(url_for('authy.signin'))

@authy.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        usersin = User.query.filter_by(email=email).first()
        if usersin:
            flash('Email already exists', category='error')
        elif len(username) < 3:
            flash('Username must be greater than 3 characters', category='error')
        elif len(password) < 6:
            flash('Password must be atleast 6 characters', category='error')
        else:
            usersin = User(email=email, username=username, password=generate_password_hash(password, method='sha256'))
            db.session.add(usersin)
            db.session.commit( )

            flash('Account created', category='success')
            login_user(usersin, remember=True)
            return redirect(url_for('views.forum'))

    return render_template("signup.html", user=current_user)