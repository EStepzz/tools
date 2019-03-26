from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///' + os.path.join(basedir,'zdnstools.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY']='123123123'
db = SQLAlchemy(app)
app.debug = True




from tools.licenses import tool_app
app.register_blueprint(tool_app)