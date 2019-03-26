import sqlite3
from tools import db
import os
from passlib.apps import custom_app_context as pwd_context
from sqlalchemy  import Column,String,create_engine ,INTEGER
from tools.logger import Log
basedir = os.path.abspath(os.path.dirname(__file__))
db_name = os.path.join(basedir,'zdnstools.db')

class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    passwd = db.Column(db.String(64))
    email = db.Column(db.String(64))
    time = db.Column(db.String(32))
    # def __init__(self,username,passwd,email,time):
    #     self.username = username
    #     self.passwd = passwd
    #     self.email = email
    #     self.time = time

    # def __repr__(self):
    #     return "{},{},{}".format(self.username,self.passwd,self.email)
    def hash_password(self,password):
        self.passwd = pwd_context.encrypt(password)
    def verify_password(self,password):
        return pwd_context.verify(password,self.passwd)

class License(db.Model):
    __tablename__ = 'license'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64))
    license_str = db.Column(db.String(128))
    project_name = db.Column(db.String(128))
    time = db.Column(db.String(28))

    # def __init__(self, username,license_str,project_name,time ):
    #     self.username = username
    #     self.license_str = license_str
    #     self.project_name = project_name
    #     self.time = time
    #
    # def __repr__(self):
    #     return self.name

class Rootpw(db.Model):
    __tablename__ = 'rootpw'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    encode_pw = db.Column(db.String(32))
    decode_pw = db.Column(db.String(32))
    project_name = db.Column(db.String(128))
    time = db.Column(db.String(28))

    # def __init__(self,username,project_name,time):
    #     self.username = username
    #     self.project_name = project_name
    #     self.time = time
    #
    # def __repr__(self):
    #     return self.encode_pw



#db.create_all()

#
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base()
# class User(Base):
#     __tablename__='user'
#     id = Column(INTEGER(16),primary_key=True)
#     name = Column(String(16))
#     passwd = Column(String(16))
#     email = Column(String(32))
#
#     def hash
#
# engine = create_engine(db_name)
# DB_Session = sessionmaker(bind=engine)