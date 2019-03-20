from flask import Flask, request, render_template, redirect, url_for, make_response
from flask_sqlalchemy import SQLAlchemy
import os

from flask_login import LoginManager
from config import Config
from flask_migrate import Migrate,MigrateCommand

app = Flask(__name__)
app.config.from_object(Config)
login_manager = LoginManager()
login_manager.init_app(app)

db = SQLAlchemy(app)
migrate = Migrate(app,db)
login = LoginManager(app)
login.login_view = 'login'

@app.before_first_request
def create_tables():
  db.create_all()

#circular imports.
#routes module needs to import the app variable defined in this script,
#so putting one of the reciprocal imports at the bottom avoids the error
#that results from the mutual references between these two files.
from app import routes, models
