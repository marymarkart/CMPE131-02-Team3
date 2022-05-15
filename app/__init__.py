from flask import Flask
from flask_sqlalchemy import SQLAlchemy

myapp_obj = Flask(__name__) 
import os

basedir = os.path.abspath(os.path.dirname(__file__))

myapp_obj.config.from_mapping(
    SECRET_KEY='you-will-never-guess',
    SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(basedir, 'app.db')
)

UPLOAD_FOLDER = '/uploads'
myapp_obj.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(myapp_obj)

from app import routes, models, forms