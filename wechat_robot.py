#!/usr/bin/python
#coding=utf8



import hashlib;
import requests;
import urllib
import re
import json

import time

# 小i
def get_reply(data):
    # print( data)
    ini_url = '''http://i.xiaoi.com/robot/webrobot?&callback=__webrobot_processMsg&data=%7B%22sessionId%22%3A%22c5a174da70a71be26a%22%2C%22robotId%22%3A%22webbot%22%2C%22userId%22%3A%22c4609cdc24a623d54b8be%22%2C%22body%22%3A%7B%22content%22%3A%22%E7%AE%97%E6%B3%95%22%7D%2C%22type%22%3A%22txt%22%7D&ts=1616252695681'''

    s = requests.Session()

    r = s.get(ini_url)
    texts = r.text.split(';')
    for text in texts[:-1]:
        res = json.loads(text[22:-1])
        print(res['userId'])
    data = {"sessionId":res['sessionId'],"robotId":"webbot","userId":res['userId'],"body":{"content":"百度"},"type":"txt"}
    url = 'http://i.xiaoi.com/robot/webrobot?&callback=__webrobot_processMsg&data='+ json.dumps(data); 
    r = s.get(url)
    print(r.text)

    


get_reply("111")