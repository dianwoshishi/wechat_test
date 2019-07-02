#!/usr/bin/python
#coding=utf8



import itchat
import hashlib;
import requests;
import urllib
import re


import time

import core.core as cc

cc.set_sys_code();


def get_response(msg, FromUserName):
    api_url = 'http://www.tuling123.com/openapi/api'
    apikey = 'e717eab0c92e408db1521d3fc2b8f6c6'
    # data中有userd才能实现上下文一致的聊天效果。
    hash = hashlib.md5()
    userid = hash.update(FromUserName.encode('utf-8'))
    data = {'key': apikey,
            'info': msg,
            'userid': userid
            }
    try:
        req = requests.post(api_url, data=data).json()
        return req.get('text')
    except:
        return


# 小i
def get_reply(data, FromUserName):
    print data
    ini = "{'sessionId':'a2203fd5749b4ba79337f85a6976eefe','robotId':'webbot','userId':'9db87549cdec4c819d336d45a138c31b','body':{'content':'" + str(
        data) + "'},'type':'txt'}&ts=1561822333832"
    url = "http://i.xiaoi.com/robot/webrobot?&callback=__webrobot_processMsg&data=" + urllib.quote(ini)
    cookie = {"cnonce": "982853", "sig": "b8d21fb095fec631c077b8fadd60a532406f3ab1",
              "XISESSIONID": "1gd925i6kl9b21rzj6cj5d6zxt", "nonce": "968762", "hibext_instdsigdip2": "1"}
    print  url
    r = requests.get(url, cookies=cookie)
    print(r.text)
    pattern = re.compile(r'\"fontColor\":0,\"content\":\"(.*?)\",')
    result = pattern.findall(r.text)
    # result[0] = result[0].replace('\r\n', '\n')
    print result
    print(result[0])
    return result[0]


# 适合 个人间聊天
@itchat.msg_register(['Text', 'Map', 'Card', 'Note', 'Sharing'])
def Tuling_robot(msg):
    print msg
    respones = get_reply(msg['Content'], msg['FromUserName'])
    itchat.send(respones, msg['FromUserName'])

# 返回图片，录音，视频
@itchat.msg_register(['Picture', 'Recording', 'Attachment', 'Video'])
def download_files(msg):
    fileDir = '%s%s' % (msg['Type'], int(time.time()))
    msg['Text'](fileDir)
    itchat.send('%s received' % msg['Type'], msg['FromUserName'])
    itchat.send('@%s@%s' % ('img' if msg['Type'] == 'Picture' else 'fil', fileDir), msg['FromUserName'])

# 自动同意陌生人好友申请
@itchat.msg_register('Friends')
def add_friend(msg):
    itchat.add_friend(**msg['Text'])
    itchat.send_msg('Nice to meet you!', msg['RecommendInfo']['UserName'])





itchat.auto_login(hotReload=True)







# itchat.dump_login_status()

friends = itchat.get_friends(update=True)[:]

# echart_pie(friends)

cc.word_cloud(friends)

itchat.run()
