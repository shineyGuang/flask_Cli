#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
# Author Xu Junkai
# coding=utf-8
# @Time    : 2020/10/31 13:40
# @Site    :
# @File    : day_zero_time.py
# @Software: PyCharm
"""
import datetime
import time
from dateutil.relativedelta import relativedelta


def get_day_zero_time() -> tuple:
    """
    获取到今日凌晨的秒数
    :return: 当前时间到今日凌晨所剩的秒数
    """
    now = datetime.datetime.now()
    date_zero = datetime.datetime.now().replace(year=now.year, month=now.month,
                                                day=now.day, hour=23, minute=59, second=59)
    date_zero_time = time.mktime(date_zero.timetuple())
    return now.strftime('%Y-%m-%d'), round(date_zero_time - time.time())


def current_last_datetime(day):
    """
    获取年月日时分秒 区间
    :param day:30 ('2020-01-09 00:00:00', '2021-01-08 23:59:59')
    :return:
    """
    current_date, _ = get_day_zero_time()
    str_current_datetime = current_date + ' 23:59:59'
    trans_str_datetime = current_date + ' 00:00:00'
    trans_datetime = datetime.datetime.strptime(trans_str_datetime, "%Y-%m-%d %H:%M:%S")
    last30_datetime = trans_datetime - relativedelta(days=+day)
    str_last30_datetime = last30_datetime.strftime('%Y-%m-%d %H:%M:%S')
    return str_last30_datetime, str_current_datetime
if __name__ == '__main__':
    print(current_last_datetime(365))
