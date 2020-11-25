# encoding:utf-8
import os

from logging.config import dictConfig

DEBUG = True
SERVER_PORT = 5000
SECRET_KEY = os.urandom(24)
SQLALCHEMY_TRACK_MODIFICATIONS = True


# DATABASE CONFIG for mysql
HOSTNAME = '10.67.118.210'
DB_PORT = '3306'
DATABASE = 'test'
USERNAME = 'root'
PASSWORD = 'password'
SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, DB_PORT,
                                                                               DATABASE)

# CACHE CONFIG for redis
REDIS_HOST = '10.67.118.210'
CACHE_TYPE = 'redis'
CACHE_REDIS_PORT = 6379
CACHE_REDIS_DB = 0
CACHE_REDIS_PASS = ""
REDIS_URL = "{}://:{}@{}:{}/{}".format(CACHE_TYPE, CACHE_REDIS_PASS, REDIS_HOST, CACHE_REDIS_PORT, CACHE_REDIS_DB)

# MESSAGE QUEUE CONFIG for rabbitMQ
MQ_HOST = "10.67.118.210"
MQ_PORT = 5432

# logging config
dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})