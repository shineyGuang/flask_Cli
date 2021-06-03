#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
# Author Xu Junkai
# coding=utf-8
# @Time    : 2020/6/26 11:51
# @Site    :
# @File    : jwt.py
# @Software: PyCharm
"""
import logging
import base64, hmac, json, time
import copy
from flask import request, abort, current_app

from utils.response_body.base_response_status.base_response_status import AuthFailed
from utils.response_body.response_code_msg.response_code_msg import ResponseMessage

logger = logging.getLogger(__name__)


class Jwt:
    def __init__(self):
        pass

    @staticmethod
    def encode(payload, key, exp, delay):
        header = {"alg": "HS256", "typ": "JWT"}
        header_j = json.dumps(header, separators=(",", ":"), sort_keys=True)
        # 使用自定义的b64encode方法进行加密
        header_bs = Jwt.b64encode(header_j.encode())
        payload = copy.deepcopy(payload)
        payload["exp"] = int(time.time()) + exp# int(time.time())
        payload["delay"] = int(time.time()) + delay
        payload_j = json.dumps(payload, separators=(",", ":"), sort_keys=True)
        payload_bs = base64.urlsafe_b64encode(payload_j.encode())
        to_sign_str = header_bs + b"." + payload_bs
        if isinstance(key, str):
            key = key.encode()
        hmac_obj = hmac.new(key, to_sign_str, digestmod="SHA256")
        sign = hmac_obj.digest()
        sign_bs = Jwt.b64encode(sign)
        return header_bs + b"." + payload_bs + b"." + sign_bs

    # jwt解密方法，返回payload
    @staticmethod
    def decode(token, key):
        """
        校验token
        :param token:
        :param key:
        :return:
        """
        header_bs, payload_bs, sign = token.split(b".")

        if isinstance(key, str):
            key = key.encode()
        hmac_obj = hmac.new(key, header_bs + b"." + payload_bs, digestmod="SHA256")
        new_sign = Jwt.b64encode(hmac_obj.digest())
        if sign != new_sign:
            logger.error(ResponseMessage.TokeninvalidErr)
            raise AuthFailed(message=ResponseMessage.TokeninvalidErr)
        payload_j = Jwt.b64decode(payload_bs)
        payload = json.loads(payload_j)
        exp = payload["exp"]
        now = int(time.time())
        if now > exp:
            delay = payload["delay"]
            if now > delay:
                logger.error(ResponseMessage.TokenTimeOutErr)
                raise AuthFailed(message=ResponseMessage.TokenTimeOutErr)
            else:
                identity = {'account_name': payload["account_name"],'id': payload["id"], 'role_id': None, 'time_stamp': now}
                token = Jwt.encode(identity, key, current_app.config["EXP"], current_app.config["DELAY"])
                abort(401, {"flush_token": token.decode("utf-8")})

        return payload

    @staticmethod
    def b64encode(s):
        return base64.urlsafe_b64encode(s).replace(b"=", b"")

    @staticmethod
    def b64decode(bs):
        rem = len(bs) % 4
        bs += b"=" * (4 - rem)
        return base64.urlsafe_b64decode(bs)
