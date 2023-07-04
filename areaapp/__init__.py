#order of importation
#python 3rd party package #local imports
from flask import Flask
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

csrf=CSRFProtect()

def createapp():
    app=Flask(__name__)
    # from areaapp import config
    # app.config.from_pyfile('config.py',silent=True)
    # from areaapp.models import db
    # db.init_app(app)
    # csrf.init_app(app)
    # migrate=Migrate(app,db)
    return app
app=createapp()



# app=Flask(__name__)

# from fapp import config
# app.config.from_pyfile('config.py',silent=False)

# db=SQLAlchemy(app)
# csrf=CSRFProtect(app)
#load the routes here
from areaapp import routes,adminroutes
#load the form
from areaapp import forms,models