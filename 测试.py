import sys

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
import os
js = "window.scrollTo(0,10000)"


option = ChromeOptions()
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-shm-usage')
web = webdriver.Chrome(options=option)
print('正在截图中...')
web.set_window_size(1920, 1080)
web.execute_script(js)
web.get('https://baike.baidu.com/item/'+'栗山未来')
img = web.find_element(By.XPATH, '/html/body/div[3]/div[2]').screenshot_as_png
with open('I:/mirai/cs.png', 'wb+') as f:
    f.write(img)
    print('搜索完成')



