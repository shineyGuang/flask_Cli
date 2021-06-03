#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
# Author Xu Junkai
# coding=utf-8
# @Time    : 2020/12/4 15:37
# @Site    :
# @File    : date_slice.py
# @Software: PyCharm
"""

import datetime
import pandas as pd


def last_day_of_month(any_day):
    """
    获取获得一个月中的最后一天
    :param any_day: 任意日期
    :return: datetime
    """
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)  # this will never fail
    return (next_month - datetime.timedelta(days=next_month.day)).strftime("%Y-%m-%d")


def date_fmt_times(start, end):
    """
    格式化 年 月 日 时 分 秒
    :param start:
    :param end:
    :param end:
    :return:
    """
    start_time = start + "-1 00:00:00"
    end_year = end.split("-")[0]
    end_month = end.split("-")[1]
    end = last_day_of_month(datetime.date(int(end_year), int(end_month), 1))
    end_time = end + " 23:59:59"
    return start_time, end_time


def pandas_date_slice(start, end):
    """
    根据时间获取年月区间
    :param start: 起始时间 2020-10-10 10:10:10
    :param end: 结束时间 2021-01-10 10:10:10
    :return:
    """
    st = start.split(" ")[0]
    ed = end.split(" ")[0]
    is_ed = ed.rsplit("-", 1)[0]
    result = pd.date_range(st, ed, freq="M")
    resule_range = [str(i).rsplit("-", 1)[0] for i in result]
    if is_ed not in resule_range:
        resule_range.append(is_ed)
    return resule_range


def date_slice(int_nums):
    """
    获取当前时间n月的连续年月
    :param int_nums: 月
    :return:
    """
    now = datetime.datetime.now()
    # 得到今年的的时间 （年份） 得到的today_year等于2016年
    today_year = now.year
    # 今年的时间减去1，得到去年的时间。last_year等于2015
    last_year = int(now.year) - 1
    # 得到今年的每个月的时间。today_year_months等于1 2 3 4 5 6 7 8 9，
    today_year_months = range(1, now.month + 1)
    # 得到去年的每个月的时间  last_year_months 等于10 11 12
    last_year_months = range(now.month + 1, 13)
    # 定义列表去年的数据
    data_list_lasts = []
    # 通过for循环，得到去年的时间夹月份的列表
    # 先遍历去年每个月的列表
    for last_year_month in last_year_months:
        # 定义date_list 去年加上去年的每个月
        date_list = "%s-%s" % (last_year, last_year_month)
        # 通过函数append，得到去年的列表
        data_list_lasts.append(date_list)

    data_list_todays = []
    # 通过for循环，得到今年的时间夹月份的列表
    # 先遍历今年每个月的列表
    for today_year_month in today_year_months:
        # 定义date_list 去年加上今年的每个月
        str_month = (
            "0{}".format(today_year_month)
            if len(str(today_year_month)) == 1
            else str(today_year_month)
        )
        data_list = "%s-%s" % (today_year, str_month)
        # 通过函数append，得到今年的列表
        data_list_todays.append(data_list)
    # 去年的时间数据加上今年的时间数据得到年月时间列表
    data_year_month = data_list_lasts + data_list_todays
    data_year_month.reverse()
    return data_year_month[:int_nums]


def date_day_slice(days):
    """
    获取当前时间n日的连续年月日
    :param days: 日
    :return:
    """
    now = datetime.datetime.now()
    day_list = []
    for day in range(0, days):
        sub_day = (now - datetime.timedelta(days=day)).strftime("%Y-%m-%d")
        day_list.append(sub_day)
    return day_list


def current_week_slice(days):
    """
    当前时间n周前
    :param days: 日
    :return:
    """
    slice_weeks = date_day_slice(days)
    week_start_date, week_end_date = slice_weeks[-1], slice_weeks[0]
    week_start_time = week_start_date + " 00:00:00"
    week_end_time = week_end_date + " 23:59:59"
    slice_weeks.reverse()
    return week_start_time, week_end_time, slice_weeks


def current_month_slice(months):
    """
    当前时间n月前
    ('2020-8-1 00:00:00', '2021-01-31 23:59:59')
    :param months:月份
    :return:
    """
    slice_months = date_slice(months)
    month_start_date, month_end_date = slice_months[-1], slice_months[0]
    month_start_time = month_start_date + '-1 00:00:00'
    fmt_month_end_datetime = datetime.datetime.strptime(month_end_date, "%Y-%m")
    month_end_datetime = last_day_of_month(fmt_month_end_datetime)
    month_end_time = month_end_datetime + " 23:59:59"
    slice_months.reverse()
    return month_start_time, month_end_time, slice_months


def get_current_last_date():
    """
    上月 本月：年月日时分秒
    :return:
    """
    currnet_str, last_str_date_start = date_slice(2)

    last_datetime = datetime.datetime.strptime(last_str_date_start, "%Y-%m")
    last_str_end = last_day_of_month(last_datetime)
    last_str_time_start = last_str_date_start + "-1 00:00:00"
    last_str_time_end = last_str_end + " 23:59:59"

    current_datetime = datetime.datetime.strptime(currnet_str, "%Y-%m")
    current_str_end = last_day_of_month(current_datetime)
    current_str_time_start = currnet_str + "-1 00:00:00"
    current_str_time_end = current_str_end + " 23:59:59"
    return current_str_time_start, current_str_time_end, current_datetime.month, last_str_time_start, last_str_time_end


def min_nums(startTime, endTime):
    """
    计算两个时间点之间的分钟数
    :param startTime: 起始时间
    :param endTime: 终止时间
    :return:
    """
    total_seconds = (endTime - startTime).total_seconds()
    mins = total_seconds / 60
    return int(mins)


if __name__ == '__main__':
    # print(current_week_slice(7))
    # print(date_slice(7))
    print(current_month_slice(5))
    # print(current_month_slice(1))

    # print(date_slice(2))
    # datetime.datetime.strptime(dd, "%Y-%m-%d %H:%M:%S")
    # print(last_day_of_month(datetime.datetime.now()))
    # print(date_day_slice(7))
    # print(pandas_date_slice("2020-10-10 10:10:10", "2021-01-10 10:10:10"))
    # print(date_fmt_times("2020-10", "2021-2"))
