from jinja2 import StrictUndefined

from flask import Flask

from model import connect_to_db  # table names

app = Flask(__name__)

app.config.from_pyfile('config.py')

# Raises an error so an undefined variable doesn't fail silently
app.jinja_env.undefined = StrictUndefined

app.jinja_env.auto_reload = True

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

if __name__ == '__main__':

	app.debug = True

	connect_to_db(app)

	#DebugToolbarExtension(app)

	app.run(host='0.0.0.0')