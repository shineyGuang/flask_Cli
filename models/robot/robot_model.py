# -*- coding: utf-8 -*-
# @Time    : 2021/6/5 4:46 下午
# @Author  : ShineyZhao
# @File    : robot_model.py
# @Email   : shiney_zhao@163.com
from sqlalchemy import Column, Integer, String, Text, TEXT, UnicodeText, Date

from models.base.base import BaseDataModel


class RobotModel(BaseDataModel):
    """
    ROTBOTS 机器人应用
    """
    id = Column(Integer, primary_key=True, comment="机器人id")
    name = Column(String(50), nullable=False, comment="机器人名称")
    pub_id = Column(Integer, nullable=False, comment="发布者")
    download_count = Column(Integer, nullable=True, comment="下载次数")
    image = Column(Text, nullable=True, comment="图标")
    oss_url = Column(Text, nullable=False, comment="Oss下载地址")
    category_id = Column(Integer, nullable=False, default=3, comment="类别id")

    def keys(self):
        return ["id", "name", "pub_id", "download_count", "image", "category_id", "create_time", "update_time"]

    def __str__(self):
        return "<RobotModel {}>".format(self.id)


class RobotDetailsModel(BaseDataModel):
    """
    ROBOTINFO 机器人详情表
    """
    id = Column(Integer, primary_key=True, comment="机器人详情id")
    content = Column(UnicodeText, nullable=True, comment="机器人详情描述")
    cur_version = Column(String(100), comment="当前版本")
    video = Column(Text, nullable=True, comment="当前版本")
    robot_id = Column(Integer, nullable=False, comment="机器人id")

    def keys(self):
        return ["id", "content", "cur_version", "video", "robot_id", "create_time", "update_time"]


class RobotUpdateModel(BaseDataModel):
    """
    RobotUpdateInfo 机器人更新历史
    """
    id = Column(Integer, primary_key=True, comment="更新id")
    robot_id = Column(Integer, nullable=False, comment="机器人id")
    version = Column(String(50), nullable=False, comment="版本")

    def keys(self):
        return ["id", "robot_id", "version", "create_time", "update_time"]
