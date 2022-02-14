import time

import requests


# 接受消息
def get_message():
    msg = requests.request('get', url + f'/fetchMessage?sessionKey={session[0]}&count=10')
    if not bool(msg.json()['data']):
        pass
    else:
        for i1 in msg.json()['data']:
            try:
                try:
                    print(i1['messageChain'][1]['text'])
                except:
                    print(i1['messageChain'][1]['imageId'])
            except:
                pass





session = []
# 取得session
data = dict(verifyKey='daisy')
url = 'http://127.0.0.1:8080/'
resp = requests.request('post', url + 'verify', json=data, )
session.append(resp.json()['session'])
print('session获取成功', session[0])
print('尝试连接中....')
# 将获取的session与bot绑定
data_session = dict(sessionKey=session[0], qq=2317387881)
resp2 = requests.request('post', url + 'bind', json=data_session)
if 'success' in resp2.text:
    print('连接成功！')
if '2' in resp2.text:
    print('指定的bot不存在')
# 获取群列表，监听指定名单的群
resp3 = requests.request('get', url + f'/groupList?sessionKey={session[0]}')
print('获取到', len(resp3.json()['data']), '个群')
for i in resp3.json()['data']:
    if '735863298' in str(i):
        print('开始监听', i['name'], i['id'])

        while '735863298' in str(i):
            get_message()
            time.sleep(2.5)
            continue








# 释放session缓存（仅测试阶段使用）
response = requests.request('post', url + 'release', json=data_session).text
if 'success' in response:
    print('session释放成功')

