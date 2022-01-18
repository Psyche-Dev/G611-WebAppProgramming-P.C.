from flask import Blueprint, render_template

authy = Blueprint('authy', __name__)

@authy.route('/signin')
def signin():
    return render_template("signin.html")

@authy.route('/signout')
def signout():
    return "<p>signout</p>"

@authy.route('/signup')
def signup():
    return render_template("signup.html")