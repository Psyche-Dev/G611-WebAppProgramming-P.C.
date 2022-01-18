import email
from flask import Blueprint, render_template, request

authy = Blueprint('authy', __name__)

@authy.route('/signin', methods=['GET','POST'])
def signin():
    return render_template("signin.html")

@authy.route('/signout')
def signout():
    return "<p>signout</p>"

@authy.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        
    return render_template("signup.html")