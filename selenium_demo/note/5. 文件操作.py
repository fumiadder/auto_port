# -*- coding: utf-8 -*-
# @Time    : 2020/5/12 15:06
# @Author  : 张开
# File      : 5. 文件操作.py





import time

from selenium import webdriver

driver = webdriver.Chrome()


driver.get('http://127.0.0.1:8022/upload/1')

time.sleep(1)
driver.find_element_by_id('ajaxFile').send_keys(r'D:\video\s28-testing-day17-接口自动化平台-实现-4\note\dengxin\data\接口测试示例-2.xlsx')
time.sleep(1)
driver.find_element_by_id('ajaxBtn').click()

time.sleep(5)
driver.quit()