import os

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG=True
class config():

    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = 'sqlite3:///' + os.path.join(basedir,'DB/zva.db')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir,'license_repository')