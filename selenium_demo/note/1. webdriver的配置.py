# -*- coding: utf-8 -*-
# @Time    : 2020/5/12 10:17
# @Author  : 张开
# File      : 1. webdriver的配置.py


# # ---------------------- Chrome ---------------------
import time
# 1. 导入webdriver
from selenium import webdriver
# 2. 实例化指定浏览器的webdriver对象
# driver = webdriver.Chrome(executable_path=r'D:\video\s28-testing-day18-selenium\note\chromedriver.exe')
driver = webdriver.Chrome()
# 3. 访问指定的url，进行相关操作
try:
    driver.get(url='https://www.baidu.com')

    driver.find_element_by_id('kw').send_keys('听雨危楼')
    driver.find_element_by_id('su').click()


# 4. 完事后，关闭浏览器
except Exception as e:
    print(e)
finally:
    time.sleep(2)
    driver.quit()



# ---------------------- Firefox ---------------------
# import time
# # 1. 导入webdriver
# from selenium import webdriver
# # 2. 实例化指定浏览器的webdriver对象
# # driver = webdriver.Chrome(executable_path=r'D:\video\s28-testing-day18-selenium\note\chromedriver.exe')
# # driver = webdriver.Firefox(executable_path=r'D:\video\s28-testing-day18-selenium\note\geckodriver.exe')
# driver = webdriver.Firefox()
# # 3. 访问指定的url，进行相关操作
# try:
#     driver.get(url='https://www.baidu.com')
#
#     driver.find_element_by_id('kw').send_keys('听雨危楼')
#     driver.find_element_by_id('su').click()
#
# # 4. 完事后，关闭浏览器
# except Exception as e:
#     print(e)
# finally:
#     time.sleep(2)
#     driver.quit()



# ------------------------- IE ------------------------

import time
# 1. 导入webdriver
from selenium import webdriver
# 2. 实例化指定浏览器的webdriver对象
# driver = webdriver.Ie(executable_path=r'D:\video\s28-testing-day18-selenium\note\IEDriverServer.exe')
driver = webdriver.Ie()
# 3. 访问指定的url，进行相关操作
try:
    driver.get(url='https://www.baidu.com')

    driver.find_element_by_id('kw').send_keys('听雨危楼')
    driver.find_element_by_id('su').click()

# 4. 完事后，关闭浏览器
except Exception as e:
    print(e)
finally:
    time.sleep(2)
    driver.quit()





