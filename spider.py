# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions

def scrien(kw, path):
    print('截图中....')
    option = ChromeOptions()
    option.add_argument('--no-sandbox')
    option.add_argument('--headless')
    web = webdriver.Chrome(options=option)
    web.set_window_size(1920, 1080)
    web.get('https://baike.baidu.com/item/' + str(kw))
    r = [web.find_element(By.XPATH, '/html/body/div[1]'), web.find_element(By.XPATH, '/html/body/div[3]/div[1]/div'),
         web.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div[2]'),
         web.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div[3]'),
         web.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div[4]'),
         web.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div[5]'),
         web.find_element(By.XPATH, '//*[@id="side_box_unionAd"]'), ]
    js = "arguments[0].remove();"
    for i in r:
        try:
            web.execute_script(js, i)
        except:
            pass
    img = web.find_element(By.XPATH, '/html/body/div[2]/div[2]/div').screenshot_as_png
    with open(path, 'wb+') as f:
        f.write(img)
        print('已保存截图,准备发送')
    web.close()
if __name__ == '__main__':
    scrien(kw='栗山未来', path='/home/daisy/临时图片.png')