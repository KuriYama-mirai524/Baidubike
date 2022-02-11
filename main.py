import requests

data = dict(verifyKey='daisy')
url = 'http://127.0.0.1:8080/verify'
resp = requests.request('post',url, json=data)
print(resp.json())
