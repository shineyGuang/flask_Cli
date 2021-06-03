# -*- coding: utf-8 -*-
# @Time    : 2021/5/20 16:37
# @Author  : 20019236
# @File    : base.py
# @Software: flaskReview
import logging
import time
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery
from contextlib import contextmanager

from sqlalchemy import Column, DateTime, func, SmallInteger, Integer

from utils.response_body.base_response_status.base_response_status import NotFound

logger = logging.getLogger(__name__)


class SQLAlchemy(_SQLAlchemy):
    """
    创建一个上下文管理器
    """

    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            db.session.rollback()
            logger.error(e)
            raise e


class Query(BaseQuery):
    """
    覆盖查询类 重写filter_by方法
    """
    def filter_by(self, **kwargs):
        if "status" not in kwargs.keys():
            kwargs["status"] = 1
        return super(Query, self).filter_by(**kwargs)

    def get_or_404(self, ident, description=None):
        rv = self.get(ident)
        if not rv:
            raise not NotFound()


db = SQLAlchemy()


class Base(db.Model):
    """
    模型的基类，为所有模型添加create_time,status属性
    方便好用，干净卫生
    """
    __abstract__ = True
    update_time = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), comment="修改时间")
    create_time = Column(DateTime(timezone=True), default=datetime.now(), comment="创建时间")
    status = Column(SmallInteger, default=1)

    def __init__(self):
        self.create_time = datetime.now()

    @property
    def create_datetime_stamp(self):
        """
        转时间戳
        :return:
        """
        if self.create_time:
            return int(time.mktime(self.create_time.timetuple()))
        else:
            return None

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != "id":
                setattr(self, key, value)

    def delete(self):
        self.status = 0

    def __getitem__(self, item):
        return getattr(self, item)


class BaseDataModel(Base):
    __abstract__ = True
    role_row_data_id = Column(Integer, comment="角色and行数据")
