#!/usr/bin/python
#coding=utf8



import hashlib;
import requests;
import urllib
import re
import json

import time

class XiaoI:
    userID = ''
    sessionID = ''
    url_base = '''http://i.xiaoi.com/robot/webrobot?&callback=__webrobot_processMsg&data='''
    def __init__(self):
        self.session = requests.Session()

    def getID(self):
        # data = {"robotId":"webbot","body":{"content":""},"type":"txt"}
        data = {"type":"open"}
        ini_url = self.url_base + urllib.parse.quote(json.dumps(data))
        
        r = self.session.get(ini_url)
        for cookie in r.cookies:
            print(cookie.name+"\t"+cookie.value)
        texts = r.text.split(';')
        for text in texts[:-1]:
            res = json.loads(text[22:-1])
            self.userID = res['userId']
            self.sessionID = res['sessionId']
            break
    # 小i
    def get_reply(self,content):
        # print( data)
        data = {"sessionId":self.sessionID,"userId":self.userID,"robotId":"webbot","body":{"content":content},"type":"txt"}
        url = self.url_base + urllib.parse.quote(json.dumps(data))

        r = self.session.get(url)
        texts = r.text.split(';')
        for text in texts[:-1]:
            res = json.loads(text[22:-1])
            if res['type'] == 'txt':
                print(res['body']['content'])
            if res['type'] == 'appmsg':
                print(res['body']['name'] + ":" + res['body']['data'])
            # print (res)

    
i = XiaoI()
i.getID()
while(1):
    i.get_reply(input())