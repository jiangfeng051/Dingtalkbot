#!/usr/bin/python
# -*- coding: UTF-8 -*-
#date:2019/4/1
#Author:jiangfeng


import tornado.web
from tornado import gen
from tornado.concurrent import run_on_executor
from concurrent.futures import ThreadPoolExecutor
from utils.connectdb import DbConnect
from utils.dingbot import DingtalkChatbot
import json,time
import logging

# 设置logging的输出格式
logging.basicConfig(level=logging.WARNING,
                    format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S', )

class IndexHandler(tornado.web.RequestHandler):
    def post(self):
        data = json.loads(self.request.body)
        # print(data)
        #查询当前时间至前一分钟的发送告警数，如果大于20，则取消发送（钉钉机器人每分钟发送频率不能超过20条）
        db_conn = DbConnect()
        cursor= db_conn.connect()
        sql = "select count(1) from prometheus_alters  where prometheus_alters.alert_time>%s and prometheus_alters.alert_time<%s"
        cursor.execute(sql,[time.time()-60,time.time()])
        result = cursor.fetchone()
        print(result)
        if result['count(1)'] < 20:
            sql = "insert into prometheus_alters (alertname,group_count,alert_time) value (%s,%s,%s)"
            print(time.time())
            cursor.execute(sql,[data['alerts'][0]['labels']['alertname'],len(data['alerts']),time.time()])
            db_conn.close()
            #格式化报警信息
            message = {}
            content = []
            message['alertname'] = data['alerts'][0]['labels']['alertname']
            for list in data['alerts']:
                alter = {}
                if 'pod_name' in list['labels']:
                    alter['pod_name'] = list['labels']['pod_name']
                if 'node' in list['labels']:
                    alter['node'] = list['labels']['node']
                if 'namespace' in list['labels']:
                    alter['namespace'] = list['labels']['namespace']
                alter['startsAt'] = list['startsAt']
                alter['endsAt'] = list['endsAt']
                alter['annotations'] = list['annotations']
                content.append(alter)
            message['alert'] = content
            print(message)
            messages = '[' + 'alertname' + ']:' + message['alertname'] + "\n"
            for list in message['alert']:
                messages = messages + "\n"
                for k, v in list.items():
                    v = json.dumps(v)
                    messages = messages + '[' + k + ']:' + v + "\n"
            print(messages)

            ding_conn = DingtalkChatbot()

            ding_conn.send_text(messages)
        else:
            logging.error("钉钉官方限制每个机器人每分钟最多发送20条，当前消息发送频率已达到限制条件，不发送报警")
