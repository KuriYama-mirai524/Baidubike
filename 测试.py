import sys

from selenium import webdriver
from selenium.webdriver import ChromeOptions
import os
# opt = ChromeOptions()
# opt.add_argument('--headless')
# opt.add_argument('--no-sandbox')
# opt.add_argument('--disable-dev-shm-usage')
#
# web = webdriver.Chrome(options=opt)
# web.get('https://www.baidu.com')
# print(web.page_source)
p = str(os.path.abspath(sys.argv[0]))
path = str(p.strip('测试.py')+'config.txt')
with open(path, 'r') as f:
    data3 = f.readlines()
    print(data3[2].split(':')[1])


