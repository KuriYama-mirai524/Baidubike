import time
import simuse
import os
import sys
import json

# 初始话基本信息
time1 = "2022/217/9:58"
Q = ''
data1 = {"问": "", "答": "", "群号":"", "发送者": ""}

nm = 1

'''获取session'''
# 读取config配置
p = str(os.path.abspath(sys.argv[0])).replace('\\', '/')  # 获取当前文件的绝对路径,用replace将\替换为/
path = p.split('/')[-1]
RealPath = p.replace(path, '')

with open(p.replace(path, 'data.json'), 'r') as f:
    config = json.loads(f.read())  # 打开配置文件,加载成json
session = simuse.Get_Session(data=config, getsession=1)  # 调用接口返回session
code = simuse.Check_Session(host=config['host'], session=session, qq=config['qq'])  # 根据code判断连接是否成功
if code == 0:
    print('建立会话成功,已连接到bot')
    print('开始监听会话')
else:
    print('连接失败,请检查host设置')
nb = 1
while 1 + 1 == 2:  # 任意填写,只要属性为True
    try:
        msg = simuse.Fetch_Message(data=config, deal=0, session=session)  # 调用接口,返回接收到的消息
    except:
        print('检测到非文本,跳过')

    for i in msg:
        print(i)
        try:
            user = i['sender']['id']
            groupid = i['sender']['group']['id']
            QA = i['messageChain'][1]['text']  # 取得群聊消息的文本
            data = QA
            if str(groupid) in str(config['group']):
                if nb / 2 == 0.5:  # 判断number是否为奇数,如果为奇数,则优先将文本添加到问题属性
                    if bool(data1['问']):  # 判断答案属性是否为空,如果不为空,则添加下一个消息到答案属性
                        '''当答案和问题一样时,忽略掉,将程序挂起,直到下一个问题与答案不一样的发言'''
                        data1['答'] = data
                        while data1["问"] == data1['答'] or not bool(data1['答']):
                            print('已挂起')
                            break
                        else:
                            data1['群号'] = groupid
                            data1['发送者'] = user
                            print(data1)
                            with open(RealPath + '词库测试.json', mode='a+') as f:
                                f.write(str(data1) + '\n')
                                nm -= 1
                                print('保存完成')
                                data1['问'] = data
                    else:
                        data1['问'] = data  # 如果问题属性为空,则为它添加问题内容
                        print(data1)
                        nb += 1

                if nb / 2 != 0.5:  # 判断number是否为偶数,如果为偶数,则将消息添加到答案属性
                    '''当答案和问题一样时,忽略掉,将程序挂起,直到下一个问题与答案不一样的发言'''
                    while data1['问'] == data1['答'] or not bool(data1['答']):
                        print('当前无人发言, 已挂起')
                        nb -= 1
                        break


        except:
            pass

    time.sleep(1)
# if str(groupid) in str(config['group']):
#                 if nb / 2 == 0.5:  # 判断number是否为奇数,如果为奇数,则优先将文本添加到问题属性
#                     if bool(list(data1)):  # 判断答案属性是否为空,如果不为空,则添加下一个消息到答案属性
#                         '''当答案和问题一样时,忽略掉,将程序挂起,直到下一个问题与答案不一样的发言'''
#                         while list(data1) == data1[data]['答']:
#                             print('已挂起')
#                             break
#                         else:
#                             Q = data
#                             print(data1)
#                             with open(RealPath + '词库测试.json', mode='a+') as f:
#                                 f.write(json.dumps(data1))
#                                 nm -= 1
#                                 print('保存完成')
#                                 Q = data
#                     else:
#                         print('设置q')
#                         Q = data  # 如果问题属性为空,则为它添加问题内容
#                         print(data1)
#                         nb += 1
#                         time.sleep(2)
#
#                 if nb / 2 != 0.5:  # 判断number是否为偶数,如果为偶数,则将消息添加到答案属性
#                     '''当答案和问题一样时,忽略掉,将程序挂起,直到下一个问题与答案不一样的发言'''
#                     while data1[Q]["答"] == Q or not bool(Q):
#                         print('当前无人发言, 已挂起')
#                         time.sleep(1)
#                         break
#
#                     else:
#                         Q = data
#                         print(data1)
#                         '''保存一个问答列表,此时的列表应当同时包含问题和答案'''
#                         with open(RealPath+'词库测试.json', mode='a+') as f:
#                             f.write(json.dumps(data1))
#                             nm -= 1
#                             print('保存完成')
#                             Q = data  # 将答案赋值为下一个发言的问题,实现循环
