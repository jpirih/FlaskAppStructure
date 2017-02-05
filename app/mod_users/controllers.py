from flask import Blueprint, request, url_for, redirect, render_template, flash, session, g

from app import db, bcrypt
from app.mod_users.decorators import requires_login
from app.mod_users.forms import LoginForm
from app.mod_users.models import User

# Blueprint definition
users = Blueprint('users', __name__, url_prefix='/users')

# before request load user
@users.before_request
def get_user():
    g.user = None
    if session['user_id']:
        g.user = User.query.get(session['user_id'])


# route definitions controller
@users.route('/dashboard')
@requires_login
def dashboard():
    return render_template('users/dashboard.html')


@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['user_id'] = user.id
            flash('Welcome {}'.format(user.name))
            return redirect(url_for('users.dashboard'))
        flash('Invalid credentials. Please try again')
    return  render_template('users/login.html', form=form)


@users.route('/logout')
def logout():
    session['user_id'] = None
    flash('You were successfully logged out.')
    return redirect(url_for('root.index'))