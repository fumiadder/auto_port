# -*- coding: utf-8 -*-
# @Time    : 2020/5/12 15:18
# @Author  : 张开
# File      : 7. 等待机制.py


# ----------------- 为什么需要等待机制 -------------

# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com")
# driver.find_element_by_id("kw").send_keys("听雨危楼-cnblogs")
# driver.find_element_by_id("su").click()
# # import time
# # time.sleep(3)
# driver.find_element_by_link_text("听雨危楼 - 博客园").click()
# driver.quit()


# ------------------------ 显式等待 ----------------

# import time
# from selenium.webdriver.support.wait import WebDriverWait   # 显式等待
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome()
# wait = WebDriverWait(driver=driver, timeout=0.1, poll_frequency=0.01)  # 在超时时间之内，我每0.5秒“看一眼”指定标签渲染成功没有
#
# driver.get("https://www.baidu.com")
# driver.find_element_by_id("kw").send_keys("听雨危楼-cnblogs")
# driver.find_element_by_id("su").click()
# wait.until(EC.visibility_of_element_located((By.LINK_TEXT, '听雨危楼 - 博客园')), "没找到").click()  # 直到标签加载完成
# # driver.find_element_by_link_text("听雨危楼 - 博客园").click()
# time.sleep(3)
# driver.quit()


# ------------------- 隐式等待 -----------------

import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(time_to_wait=10)

driver.get("https://www.baidu.com")
driver.find_element_by_id("kw").send_keys("听雨危楼-cnblogs")
driver.find_element_by_id("su").click()
driver.find_element_by_link_text("听雨危楼 - 博客园").click()
time.sleep(3)
driver.quit()
















