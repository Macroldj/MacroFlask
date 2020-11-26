# encoding:utf-8
import os

from logging.config import dictConfig

DEBUG = True
SERVER_PORT = 5000
SECRET_KEY = os.urandom(24)

# DATABASE CONFIG for mysql
HOSTNAME = '49.234.134.105'
DB_PORT = '3306'
DATABASE = 'test'
USERNAME = 'root'
PASSWORD = 'root'
SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, DB_PORT, DATABASE)
# SQLALCHEMY_DATABASE_URI = "sqlite:////test.db"
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_POOL_SIZE = 10
SQLALCHEMY_MAX_OVERFLOW = 5

# CACHE CONFIG for redis
REDIS_HOST = '49.234.134.105'
CACHE_TYPE = 'redis'
CACHE_REDIS_PORT = 6379
CACHE_REDIS_DB = 0
CACHE_REDIS_PASS = ""
CACHE_REDIS_MAX_CONN = 20
REDIS_URL = "{}://:{}@{}:{}/{}".format(CACHE_TYPE, CACHE_REDIS_PASS, REDIS_HOST, CACHE_REDIS_PORT, CACHE_REDIS_DB)

# MESSAGE QUEUE CONFIG for rabbitMQ
MQ_HOST = "49.234.134.105"
MQ_PORT = 5672

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