# -*- coding: utf-8 -*-
# @Time    : 2021/5/20 15:31
# @Author  : 20019236
# @File    : __init__.py.py
# @Software: flaskReview
import logging.config
import os

import yaml
from flask_compress import Compress

from .services import Flask
from flask_cors import CORS

from globals.bp_v1_manage import bp_v1
from server.config.settings import envs
from models.base.base import db
from models.users.users_model import UsersAuthModel, UsersInfoModel


def config_init(app, environ):
    try:
        config_obj = envs.get(environ)
        config_obj.init_app(app)
        print(f"【Zcg_Server】初始化配置成功！")
    except Exception as e:
        print(f"【Zcg_Server】初始化配置失败！")


def log_init(app):
    if not os.path.exists(app.config['LOGGING_PATH']):
        os.mkdir(app.config['LOGGING_PATH'])
    try:
        with open(app.config['LOGGING_CONFIG_PATH'], 'r', encoding='utf-8') as f:
            dict_conf = yaml.safe_load(f.read())
        logging.config.dictConfig(dict_conf)
        print(f"【Zcg_Server】初始化日志成功！")
    except Exception as e:
        print(f"【Zcg_Server】初始化日志失败！")


def mysql_init(app):
    """
    初始化mysql
    :param app:
    :return:
    """
    db.app = app
    db.init_app(app)
    with app.app_context():
        db.create_all()
    print(f"【Zcg_Server】初始化MySQL成功！")


def register_blueprints(app):
    version = app.config.get("VERSION")
    url_prefix = f"/api/{version}"
    app.register_blueprint(
        bp_v1,
        url_prefix=url_prefix
    )


def create_app(environ):
    """
    初始化app
    :param environ:
    :return:
    """
    app = Flask(__name__)
    # 初始化配置
    config_init(app, environ)
    # 初始化日志
    log_init(app)
    # 初始化mysql
    mysql_init(app)
    # 挂载蓝图
    register_blueprints(app)
    # 跨域
    CORS(app, supports_credentials=True, resources=r'/*')
    # 数据压缩
    Compress(app)
    return app
