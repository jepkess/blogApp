from flask import render_template,redirect,url_for, flash,request
from flask_login import login_user,login_required,logout_user
from . import auth
from ..models import User
from .forms import RegistrationForm,LoginForm
from .. import db
from ..email import mail_message


@auth.route('/login', methods=['POST','GET'])
def login(): # login view function that renders the template file(login.html)
    """user login"""
    login_form=LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid email or Password')

    title = 'Blog login_form'
    return render_template('auth/login.html',login_form = login_form,title=title)



@auth.route('/register', methods=['GET','POST'])
def register(): #register view function that renders the register template file.
    registration_form = RegistrationForm()
    if registration_form.validate_on_submit():
        user= User(email=registration_form.email.data,username=registration_form.username.data,password=registration_form.password.data)
        db.session.add(user)
        db.session.commit()

        mail_message("Welcome to iBlog","/welcome_user",user.email,user=user)
        return  redirect(url_for('auth.login'))
    return render_template('auth/register.html',registration_form=registration_form)




@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
