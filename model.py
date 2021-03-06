from flask_sqlalchemy import SQLAlchemy, Model
from werkzeug.security import generate_password_hash, check_password_hash

#This is the connection to PostgreSQL database from library
#Find session object within where we do most of our interactions (like committing)

SQLALCHEMY_DATABASE_URI = "postgresql:///take-home-proj"
db = SQLAlchemy()

class User(db.Model):
	"""User of travel journal site"""

	__tablename__ = "users"

	user_id = db.Column(db.Integer, primary_key=True)
	user_name = db.Column(db.String(25), nullable=False)
	email = db.Column(db.String(64), unique=True)
	password = db.Column(db.String(), nullable=False)

	def __repr__(self):

		return f"<User user_id={self.user_id} email={self.email}>"


	def create_password(self, password):
		self.password = generate_password_hash(password)

	def is_valid_password(self, password):
		return check_password_hash(self.password, password)

class Goal(db.Model):

	__tablename__="goals"

	goal_id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
	goal = db.Column(db.String(), nullable=True)

	def __repr__(self):

		return f"<Goal goal_id={self.goal_id}>"

	goals = db.relationship("User", backref="goals")




def connect_to_db(app):
	"""Connect the database to our Flask app."""

	# Configure to use our PostgreSQL database
	# app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:{var}/take-home-proj'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	app.config['SQLALCHEMY_ECHO'] = True
	db.app = app
	db.init_app(app)



if __name__ == "__main__":

	from server import app

	connect_to_db(app)
	#db.drop_all()
	#db.create_all()

	print("Connect to DB.")
