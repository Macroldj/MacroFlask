#encoding:utf-8

import os

#开启调试模式
DEBUG = True

#session 加密
SECRET_KEY = os.urandom(24)

#数据库配置
SQLALCHEMY_TRACK_MODIFICATIONS = True

#默认数据库源
HOSTNAME = 'localhost'
PORT = '3306'
DATABASE = 'ceshi'
USERNAME = 'root'
PASSWORD = '123456'
SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)

#绑定多个数据库
'''
使用__bind_key__来绑定
class OneTable(db.Model):
    __bind_key__ = 'db_one'
    __tablename__ = 'fadfsd'
    id = db.Column(db.Integer(),primary_key=True)
    dafef = db.Column(db.DATETIME())
'''
DATABASEONE = 'discuz'
DATABASETWO = 'kuzhuan'
SQLALCHEMY_BINDS = {
    'db_one':'mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASEONE),
    'db_two':  'mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASETWO)
}
