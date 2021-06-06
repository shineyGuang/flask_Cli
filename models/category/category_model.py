# -*- coding: utf-8 -*-
# @Time    : 2021/6/5 4:39 下午
# @Author  : ShineyZhao
# @File    : category_model.py
# @Email   : shiney_zhao@163.com
from sqlalchemy import String, Column, Integer

from models.base.base import BaseDataModel


class CategoryModel(BaseDataModel):
    """
    CATEGORY 分类表
    """
    __tablename__ = "category"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, comment="分类名")

    @property
    def keys(self):
        return ["id", "name", "create_time", "update_time"]

    def __str__(self):
        return "<CategoryModel {}>".format(self.id)
