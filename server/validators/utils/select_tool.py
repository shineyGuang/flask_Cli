# -*- coding: utf-8 -*-
# @Time    : 2021/6/1 10:33
# @Author  : 20019236
# @File    : select_tool.py
# @Software: flaskReview
import logging

from wtforms import SelectField

logger = logging.getLogger(__name__)


class PreDealtSelectField(SelectField):
    """
    预处理choice字段
    """

    def pre_validate(self, form):
        for v, c in self.choices:
            if self.data == v:
                return
        logger.error(f"{self.name}不是一个有效的选择")
        raise ValueError(
            self.gettext(f"{self.name}不是一个有效的选择: {self.choices}")
        )
