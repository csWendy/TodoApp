import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'try-to-guess-and-you-will-fail'
    # setting up db config
    #'mysql://{master username}:{db password}@{endpoint}/{db instance name}'
    SQLALCHEMY_DATABASE_URI= 'mysql+pymysql://todoapp:todoapp123@todoapp.cgya4a2lrtxt.us-east-1.rds.amazonaws.com:3306/todoapp'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('todoapp:todoapp123@todoapp.cgya4a2lrtxt.us-east-1.rds.amazonaws.com:3306/todoapp') or\
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
