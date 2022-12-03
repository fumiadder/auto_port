# -*- coding: utf-8 -*-
# @Time    : 2020/5/12 11:52
# @Author  : 张开
# File      : 3. 键盘事件.py


"""
键盘的操作：
    复制/粘贴
    全选
    回车
"""
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # 用前先导入
# 如何查看 Keys 中有哪些属性可用
print(Keys.__dict__)
print(dir(Keys))
driver = webdriver.Chrome()

driver.get(url='http://www.neeo.cc:6005/login/')

obj = driver.find_element_by_id('id_username')
obj.send_keys('alex dsb')
# 全选
obj.send_keys(Keys.CONTROL, 'a')
# 复制
time.sleep(2)
obj.send_keys(Keys.CONTROL, 'c')
# 粘贴
time.sleep(1)
driver.find_element_by_id('id_password').send_keys(Keys.CONTROL, 'v')

# 回车
driver.find_element_by_id('id_password').send_keys(Keys.ENTER)

# time.sleep(3)
# driver.quit()




