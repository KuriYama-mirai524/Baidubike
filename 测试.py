from selenium import webdriver
from selenium.webdriver import ChromeOptions
opt = ChromeOptions()
opt.add_argument('--headless')
opt.add_argument('--no-sandbox')
opt.add_argument('--disable-dev-shm-usage')

web = webdriver.Chrome(options=opt)
web.get('https://www.baidu.com')
print(web.page_source)