from app import db, bcrypt
from app.mod_users import constants as user


# Base class with standard fields for every table
class Base(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

# Sample user class
class User(Base):

    __tablename__ = "users"

    name = db.Column(db.String(155), nullable=False)
    email = db.Column(db.String(155), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.SmallInteger, default=user.ADMIN)
    status = db.Column(db.SmallInteger, default=user.ACTIVE)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = bcrypt.generate_password_hash(password)

    def get_role(self):
        return user.ROLE[self.role]

    def get_status(self):
        return user.STATUS[self.status]

    def __repr__(self):
        return '<User: {} - {}>'.format(self.name, self.email)


