import os
# main config file development environment
DEBUG = True
# Projects base directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# database connection params  postgress sql
SQLALCHEMY_DATABASE_URI = "postgresql://postgres:student15@localhost/printing"
SQLALCHEMY_TRACK_MODIFICATIONS = True

# cross site request Forgery CSRF
CSRF_ENABLED = True
CSRF_SESSION_KEY = "top secret"

# application secret key
SECRET_KEY = "my-top-secret"
