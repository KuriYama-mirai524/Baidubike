import requests
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions

option = ChromeOptions()
option.add_argument('--headless')




def get_msg(keyw):
    url = 'https://zh.moegirl.org.cn/' + keyw
    resp = requests.get(url)
    html = etree.HTML(resp.text)
    res = html.xpath('//*[@id="mw-content-text"]/div/div[3]/table/tbody/tr[1]/td/div/div[2]/div/div/div/a/@href')[0]
    print('https://zh.moegirl.org.cn/' + res)
    res2 = html.xpath('')



def scrien(kw):
    option = ChromeOptions()
    print('正在截图中...')
    option.add_argument('--headless')
    web = webdriver.Chrome(options=option)
    web.set_window_size(1920, 1080)
    web.get('https://baike.baidu.com/item/'+kw)
    img = web.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[1]').screenshot_as_png
    with open('/home/daisy/img/img.png', 'wb+') as f:
        f.write(img)
        print('搜索完成')
        return img



