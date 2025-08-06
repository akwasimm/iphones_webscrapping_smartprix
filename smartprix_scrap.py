from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

s = Service("D:/OneDrive/Desktop/chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get('https://www.smartprix.com/mobiles')
driver.find_element(by=By.XPATH , value= '//*[@id="app"]/main/aside/div/div[3]/div[3]/label[11]/span').click()
time.sleep(1)
old_height = driver.execute_script('return document.body.scrollHeight')
count = 0
while True:
    driver.find_element(by = By.XPATH , value='//*[@id="app"]/main/div[1]/div[2]/div[3]').click()
    new_height = driver.execute_script('return document.body.scrollHeight')
    time.sleep(5)
    

    if old_height==new_height:
        break
    old_height = new_height
    count +=1
    print(count)
html = driver.page_source
with open('phones.html' , 'w' , encoding='utf-8') as f:
    f.write(html)


