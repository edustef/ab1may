from flask import render_template, url_for, flash, redirect, request
from application.forms import RegisterForm, LoginForm, UpdateAccountForm
from application.models import User 
from application import app, bcrypt, db
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html", title='Home')

@app.route("/login", methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember_me.data)
			flash('Succesfuly logged in', 'success')
			next_page = request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('index'))
		else:
			flash('Login unsuccesful. Please check username and password', 'danger')
	return render_template("login.html", title='Login', form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
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
	return redirect(url_for('index'))

@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
	form = UpdateAccountForm()
	if form.validate_on_submit():
		current_user.username = form.username.data
		current_user.email = form.email.data
		db.session.commit()
		flash('Your account has been succesfuly updated.', 'success')
		return redirect(url_for('account'))
	elif request.method == 'GET':
		form.username.data = current_user.username
		form.email.data = current_user.email
	avatar_img = url_for('static', filename='profile_pics/' + current_user.avatar_img)
	return render_template("account.html", title='Profile', avatar_img=avatar_img, form=form)

@app.route("/data")
@login_required
def data():
	data = User.query.all()
	return render_template("data.html", title='Data', data=data)

@app.route("/delete")
def delete():
	User.query.delete()
	db.session.commit()
	return redirect(url_for('index'))