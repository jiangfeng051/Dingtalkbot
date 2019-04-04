#!/usr/bin/python
# -*- coding: UTF-8 -*-
#date:2019/4/1
#Author:jiangfeng

import json
import requests
import time
from config import settings


class DingtalkChatbot:
    def __init__(self):
        self.headers = {'Content-Type': 'application/json; charset=utf-8'}
        self.webhook = settings.webhook['url']


    def send_text(self,msg):
        data = {'msgtype': 'text', 'text': {'content': ''}, 'isAtAll': False}
        data['text']['content'] = msg
        post_data = json.dumps(data)
        response = requests.post(self.webhook, headers=self.headers, data=post_data)
        result = response.json()
        # if result['errmsg'] == 'send too fast':
        #     print('send too fast')
        #     print(time.time())
        #     time.sleep(120)
        #     print(time.time())
        print(result)


    def send_markdown(self):
        pass


if __name__ == '__main__':
    obj = DingtalkChatbot()
    i = 1
    print(time.ctime())
    while True:
        if i%20 == 21 :
            print(time.ctime())
            time.sleep(60)
            print(time.ctime())
        else:
            obj.send_text(i)
            time.sleep(1)
        i += 1
    # while True:
    #     obj.send_text(i)
    #     i += 1