# -*- coding: utf-8 -*-
# @Time    : 2021/6/1 10:00
# @Author  : 20019236
# @File    : baseform.py
# @Software: flaskReview
import logging

from flask import request
from wtforms import Form

from utils.response_body.base_response_status.base_response_status import NotFound

logger = logging.getLogger(__name__)


class BaseForm(Form):
    """
    表单校验基类
    """

    def __init__(self):
        data = request.get_json(silent=True)
        if not data:
            data = request.form.to_dict()
        args = request.args.to_dict()
        if not data:
            print(f"args:<{args}>")
        else:
            print(f"data:<{data}>")
        super(BaseForm, self).__init__(data=data, **args)

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            logger.error(str(self.errors))
            raise NotFound(message=self.errors)
        return self
