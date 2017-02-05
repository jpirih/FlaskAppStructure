# Flask app structure 

This is only basic project structure for flask app prepared for searving with Digital oceans  Virtual machines. 
Uses Flask-SQLAlchemy ORM prepared for postgres sql db, change the config file  for proper connection details. 

main app/__init__.py  contains app object, db object and  blueprints registration. One simple blueprint created for 
example. 

This is a boiler plate so it contains only one sample module users. 
in static folder is included Bootstrap 3.3.7  

You need to set real data for SQLALCHEMY_DATABASE_URI before you uncoment
db.create_all() command in app/__init__.py 

