from flask_sqlalchemy import SQLAlchemy

#This is the connection to PostgreSQL database from library
#Find session object within where we do most of our interactions (like committing)

SQLALCHEMY_DATABASE_URI = "postgresql:///take-home"
db = SQLAlchemy()


def connect_to_db(app):
	"""Connect the database to our Flask app."""

	# Configure to use our PostgreSQL database
	app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:beguhl10@localhost:5432/take-home'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	app.config['SQLALCHEMY_ECHO'] = True
	db.app = app
	db.init_app(app)


if __name__ == "__main__":

	from server import app

	connect_to_db(app)
	#db.drop_all()
	db.create_all()

	print("Connect to DB.")
