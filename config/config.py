# encoding:utf-8
import os

DEBUG = True
SERVER_PORT = 5000
SECRET_KEY = os.urandom(24)
SQLALCHEMY_TRACK_MODIFICATIONS = True

HOSTNAME = '10.67.118.210'
DB_PORT = '3306'
DATABASE = 'test'
USERNAME = 'root'
PASSWORD = 'xiaoxiao'
# SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,DB_PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = 'sqlite:////test.db'