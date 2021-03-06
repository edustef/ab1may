from application import db, login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	avatar_img = db.Column(db.String(35), nullable=False, default='default.png')
	password = db.Column(db.String(60), nullable=False)
	posts = db.relationship('Post', backref='poster', lazy=True)

	def __repr__(self):
		return f"User('{self.username}', '{self.email}', '{self.avatar_img}')"

class Post(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

	def __repr__(self):
		return f"Post('{self.id}', '{self.date_posted}')"