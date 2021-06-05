# -*- coding: utf-8 -*-
# @Time    : 2021/5/20 15:35
# @Author  : 20019236
# @File    : settings.py
# @Software: flaskReview
import logging
import os


class BaseConfig(object):
    @classmethod
    def init_app(cls, app):
        """
        配置初始化
        :param app:
        :return:
        """
        app.config.from_object(cls)


class Config(BaseConfig):
    # 版本
    VERSION = "v1"

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    PROJECT_DIR = os.path.abspath(os.path.join(BASE_DIR, os.path.pardir))

    # logging
    LOGGING_CONFIG_PATH = "./server/config/logging_conf.yaml"
    LOGGING_PATH = os.path.join(BASE_DIR, "logs")

    # page size/number
    PAGE_NUM = "1"
    PAGE_SIZE = "10"

    # JWT SIGN
    SIGN = "#KD(S@de!,.s"
    EXP = 5 * 60 * 60
    DELAY = 60 * 60 * 24 * 5

    # FLASK-SQLALCHEMY
    SQLALCHEMY_TRACK_MODIFICATIONS = True  # 调式启动，部署关闭
    SQLALCHEMY_ECHO = True  # 调式启动，部署关闭
    SQLALCHEMY_POOL_RECYCLE = 3 * 60 * 60
    SQLALCHEMY_POOL_TIMEOUT = 10
    SQLALCHEMY_MAX_OVERFLOW = 5
    SQLALCHEMY_POOL_SIZE = 10
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True  # 连接结束后自定提交数据库中变动

    # 线程池
    # COMMON_THREDA_POOL = BoundedThreadPoolExecutor()


class DevConfig(Config):
    """开发环境下的配置"""
    DEBUG = True

    # MySQL
    DB_USERNAME = "root"
    DB_PASSWORD = ""
    DB_HOST = "127.0.0.1"
    DB_PORT = 3306
    DB_NAME = "cms_db"
    DB_URI = "mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8" % (
        DB_USERNAME,
        DB_PASSWORD,
        DB_HOST,
        DB_PORT,
        DB_NAME,
    )
    SQLALCHEMY_DATABASE_URI = DB_URI

    # Redis
    # DB_REDIS_PORT = 6379
    # DB_REDIS_HOST = "123.57.202.175"
    # DB_REDIS_DB = 1  # sso_db and current_data
    # DB_REDIS_DB2 = 5  # permission_db
    # DB_REDIS_PASSWORD = 'shiney_zhao'
    # REDIS_POOL = redis.ConnectionPool(host=DB_REDIS_HOST, port=DB_REDIS_PORT, password=DB_REDIS_PASSWORD,
    #                                   db=DB_REDIS_DB, max_connections=10,
    #                                   decode_responses=True)
    # COMMON_REDIS = redis.StrictRedis(connection_pool=REDIS_POOL)

    # Celery
    # CELERY_TIMEZONE = 'Asia/Shanghai'
    # CELERY_REDIS_DB = 2
    # CELERY_REDIS_HOST = "123.57.202.175"
    # CELERY_REDIS_PORT = "6379"
    # CELERYD_TASK_SOFT_TIME_LIMIT = 200
    # CELERY_ACCEPT_CONTENT = ['pickle', 'json', ]
    # CELERY_TASK_SERIALIZER = 'pickle'
    # CELERY_RESULT_SERIALIZER = 'pickle'


class PrdConfig(Config):
    """生产环境下配置"""
    DEBUG = False
    LOG_LEVEL = logging.WARNING


envs = {
    "dev": DevConfig,
    "prd": PrdConfig,
}
