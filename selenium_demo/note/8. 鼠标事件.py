# -*- coding: utf-8 -*-
# @Time    : 2020/5/12 16:04
# @Author  : 张开
# File      : 8. 鼠标事件.py


import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

# driver.get("http://sahitest.com/demo/clicks.htm")

time.sleep(1)

# 鼠标左键单击
# ActionChains(driver).click(driver.find_element_by_xpath('/html/body/form/input[3]')).perform()

# 鼠标左键双击
# ActionChains(driver).double_click(driver.find_element_by_xpath('/html/body/form/input[2]')).perform()

# 鼠标右键单击
# ActionChains(driver).context_click(driver.find_element_by_xpath('/html/body/form/input[4]')).perform()



# 悬浮
# driver.get("https://www.cnblogs.com/Neeo/articles/11002003.html")
# ActionChains(driver).move_to_element(driver.find_element_by_id('cb_post_title_url')).perform()


# 拖拽
driver.get('http://www.jq22.com/demo/pintu20151229/')
time.sleep(1)
driver.find_element_by_id('start').click()
time.sleep(2)
start = driver.find_element_by_xpath('//*[@id="container"]/div[1]')
end = driver.find_element_by_xpath('//*[@id="container"]/div[25]')

ActionChains(driver).drag_and_drop(start, end).perform()










time.sleep(3)
driver.quit()