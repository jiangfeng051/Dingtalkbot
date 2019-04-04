#!/usr/bin/python
# -*- coding: UTF-8 -*-
#date:2019/4/1
#Author:jiangfeng

settings = {
    'template_path': 'template',
    'static_path': 'static',
    'static_url_prefix': '/static/',
    'cookie_secret' : "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
    "login_url": "/login",
}


webhook = {
    'url': 'https://oapi.dingtalk.com/robot/send?access_token=fdbe60a7b81bed44f13135cb20c58820c0eeb2c398ba00647297c14ffa25dc15'
}


#数据库配置
PY_MYSQL_CONN_DICT = {
    "host": '192.168.112.74',
    "port": 3306,
    "user": 'root',
    "passwd": 'zentech#123',
    "db": 'k8sharbor',
    "charset": 'utf8'
}