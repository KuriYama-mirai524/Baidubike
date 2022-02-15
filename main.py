# coding=utf-8
import time

import requests
import spider
import os
import sys

p = str(os.path.abspath(sys.argv[0]))
imgpath = str(p.strip('main.py') + '临时图片.png').replace('\\', '/')
print(imgpath)
path = str(p.strip('main.py') + 'config.txt').replace('\\', '/')
print(path)

with open(path, 'r') as f:
    data3 = f.readlines()
    print(data3[0].split('\n')[0])

groupn = str(data3[2].split(':')[1].split('\n')[0])
print(groupn)


# 接受消息
def get_message():
    msg = requests.request('get', url + f'/fetchMessage?sessionKey={session[0]}&count=10')
    if not bool(msg.json()['data']):
        pass
    else:
        groupid = msg.json()['data'][0]['sender']['group']['id']
        if str(groupid) in groupn:
            for i1 in msg.json()['data']:
                try:
                    try:
                        print(i1['messageChain'][1]['text'])
                        if '百度 ' in i1['messageChain'][1]['text']:
                            ms = str(i1['messageChain'][1]['text'])
                            spider.scrien(kw=ms.split('度')[1], path=imgpath)
                            group = {'sessionKey': session[0],
                                     'group': groupn,
                                     "messageChain": [
                                         {"type": "Image", "path": imgpath}]
                                     }
                            print(group)
                            response1 = requests.request('post', url + '/sendGroupMessage', json=group)
                            print(response1.text)

                    except:
                        print(i1['messageChain'][1]['imageId'])
                except:
                    pass


session = []
# 取得session
sessionkey = str(data3[1].split(':')[1])
data = {
    'verifyKey': sessionkey.split('\n')[0]
}

print(data3[1].split(':')[1])
url = 'http://' + str(data3[0].split('\n')[0]).split('=')[1]
print(url)
resp = requests.request('post', url=url + '/verify', json=data)
print(resp.text)
session.append(resp.json()['session'])
print('session获取成功', session[0])
print('尝试连接中....')
# 将获取的session与bot绑定
data_session = dict(sessionKey=session[0], qq=data3[3].split(':')[1])
print(data_session)
resp2 = requests.request('post', url + '/bind', json=data_session)
if 'success' in resp2.text:
    print('连接成功！')
if '2' in resp2.text:
    print('指定的bot不存在')
# 获取群列表，监听指定名单的群
resp3 = requests.request('get', url + f'/groupList?sessionKey={session[0]}')
print('获取到', len(resp3.json()['data']), '个群')
for i in resp3.json()['data']:
    d = i['id']

    if str(d) in groupn:
        print('开始监听')

        while str(d) in groupn:
            get_message()
            time.sleep(1.5)
            continue
    else:
        print('未检索到群号')

# 释放session缓存（仅测试阶段使用）
response = requests.request('post', url + '/release', json=data_session).text
if 'success' in response:
    print('session释放成功')
