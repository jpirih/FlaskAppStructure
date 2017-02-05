from  flask import  Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


# app object initialization
app = Flask(__name__)

# app configurations
app.config.from_object('config')

# db object initialization
db = SQLAlchemy(app)

# bcrypt initialization
bcrypt = Bcrypt(app)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error), 404


# blueprints registration
from app.mod_root.controllers import root
from app.mod_users.controllers import users
app.register_blueprint(users)
app.register_blueprint(root)


