from flask import render_template, url_for, flash, redirect
from application.forms import RegisterForm, LoginForm
from application.models import User 
from application import app, bcrypt, db
from flask_login import login_user, current_user, logout_user

@app.route("/")
@app.route("/home")
def home():
	return render_template("index.html", title='Home')

@app.route("/login", methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username='testadmin').first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember_me.data)
			flash('Succesfuly logged in', 'success')
			return redirect(url_for('home'))
		else:
			flash('Login unsuccesful. Please check username and password', 'danger')
	return render_template("login.html", title='Login', form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = RegisterForm()
	if form.validate_on_submit():
		hash_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data, email=form.email.data, password=hash_pass)
		db.session.add(user)
		db.session.commit()
		flash(f'Your account has been succesfuly created. You can now log in.', 'success')
		return redirect(url_for('login'))
	return render_template("register.html", title='Register', form=form)

@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('home'))

@app.route("/account")
def account():