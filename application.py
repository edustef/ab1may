from flask import Flask, render_template, url_for, flash, redirect
from forms import RegisterForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'b29a5e61816e3c104500566e4909327d'

@app.route("/")
@app.route("/home")
def home():
	return render_template("index.html", title='Home')

@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'admin@gmail.com' and form.password.data == 'admin':
			flash('Succesfuly logged in', 'success')
			return redirect(url_for('home'))
		else:
			flash('Login unsuccesful. Please check username and password', 'danger')
	return render_template("login.html", title='Login', form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegisterForm()
	if form.validate_on_submit():
		flash(f'Account succesfuly created', 'success')
	return render_template("register.html", title='Register', form=form)

if __name__ == '__main__':
	app.run(debug=True)