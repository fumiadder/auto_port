# -*- coding: utf-8 -*-
# @Time    : 2020/5/12 15:12
# @Author  : 张开
# File      : 6. 滚动条操作.py




import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(time_to_wait=10)

driver.get("https://www.cnblogs.com/Neeo/p/10864123.html")

# time.sleep(3)
# driver.execute_script("window.scrollBy(0, 700)")  # 相对移动，从当前位置移动700像素
# time.sleep(3)
# driver.execute_script("window.scrollBy(0, 700)")  # 相对移动，从当前位置移动700像素，即 上次移动的700 + 本次的700 = 1400像素






# 获取当前的窗口对象
element = driver.find_element_by_tag_name('body')
time.sleep(3)
#从顶部下拉到底部
driver.execute_script("arguments[0].scrollIntoView(false);", element)  # 默认为true
time.sleep(3)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")  # 使用window对象

# 从底部拉到顶部
driver.execute_script("arguments[0].scrollIntoView(true);", element)













time.sleep(3)
driver.quit()