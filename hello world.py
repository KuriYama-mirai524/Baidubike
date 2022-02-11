from mirai import Mirai, Plain, MessageChain, Friend
import asyncio

qq = 2317387881 # 字段 qq 的值
authKey = 'daisy' # 字段 authKey 的值
mirai_api_http_locate = '127.0.0.1:8080/' # httpapi所在主机的地址端口,如果 setting.yml 文件里字段 "enableWebsocket" 的值为 "true" 则需要将 "/" 换成 "/ws", 否则将接收不到消息.

app = Mirai(f"mirai://{mirai_api_http_locate}?authKey={authKey}&qq={qq}", websocket=True)

@app.receiver("FriendMessage")
async def event_gm(app: Mirai, friend: Friend):
    await app.sendFriendMessage(friend, [
        Plain(text="Hello, world!")
    ])

if __name__ == "__main__":
    app.run()