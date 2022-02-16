from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
option = ChromeOptions()
option.add_argument('--headless')
option.add_argument('--disable-gpu')
web = webdriver.Chrome(options=option)
web.set_window_size(1920, 1080)
print(web.get_window_size())
web.get('https://baike.baidu.com/item/境界的彼方')
r = [web.find_element(By.XPATH, '/html/body/div[1]'),web.find_element(By.XPATH, '/html/body/div[3]/div[1]/div'),
web.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div[2]'),
web.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div[3]'),
web.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div[4]'),
web.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div[5]'),
web.find_element(By.XPATH, '//*[@id="side_box_unionAd"]'),]
js = "arguments[0].remove();"
for i in r:
    try:
        web.execute_script(js, i)
    except:
        pass
img = web.find_element(By.XPATH, '/html/body/div[2]/div[2]/div').screenshot_as_png
with open('E:/测试.png', 'wb+') as f:
    f.write(img)
    print('完成')
web.close()
