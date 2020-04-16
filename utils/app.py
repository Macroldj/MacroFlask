from flask import Flask

from app.user import urls
from utils.functions import init_ext
from utils.settings import TEMPLATE_DIR, STATIC_DIR


def create_app(Config):
    # 创建flask模型
    app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

    # 注册蓝图
    app.register_blueprint(blueprint=urls, url_prefix='/user')

    # 配置config
    app.config.from_object(Config)
    app.debug = True
    init_ext(app)
    return app