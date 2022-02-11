import requests


# 取得session
def get_session():
    data = dict(verifyKey='daisy')
    url = 'http://127.0.0.1:8080/'
    resp = requests.request('post', url + 'verify', json=data)
    print(resp.json())
    return resp.json()


# 将session和bot的qq号绑定
def link_start(res):
    print('尝试连接....')
    url = 'http://127.0.0.1:8080/'
    data_session = dict(sessionKey=res['session'], qq=2317387881)
    resp2 = requests.request('post', url + 'bind', json=data_session)
    if 'success' in resp2.text:
        print('连接成功！')
    if '2' in resp2.text:
        print('指定的bot不存在')

if __name__ == '__main__':
    link_start(res=get_session())


