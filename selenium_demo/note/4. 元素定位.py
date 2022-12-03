# -*- coding: utf-8 -*-
# @Time    : 2020/5/12 14:33
# @Author  : 张开
# File      : 4. 元素定位.py

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('http://www.neeo.cc:6005/login/')



try:
    # ------------------ id --------------
    # driver.find_element_by_id('id_username').send_keys('邓鑫 dsb')

    # ------------------ class --------------

    # driver.find_element_by_class_name('form-control').send_keys('邓鑫 dsb')
    # input_list = driver.find_elements_by_class_name('form-control')
    # print(input_list)
    # input_list[1].send_keys('邓鑫 dsb')

    # ------------------ tag name --------------
    # print(driver.find_element_by_tag_name('input').get_attribute('value'))

    # ------------------ name --------------
    # 首先要确保
    # driver.find_element_by_name('username').send_keys('邓鑫 dsb')


    # ------------------- link text ---------------

    # 绝对定位，完全匹配text值
    # driver.find_element_by_link_text("Tracer").click()
    # driver.find_element_by_link_text("Trace").click()  # 必须完全匹配，否则报错

    # 模糊定位,只要 text 包含 关键字 即可
    # driver.find_element_by_partial_link_text("Tracer").click()
    # driver.find_element_by_partial_link_text("Trac").click()

    # ------------------- link text ---------------
    # driver.find_element_by_xpath('//*[@id="id_username"]').send_keys('asssssssss')

    # -------------------- css selector ---------------
    # id
    # driver.find_element_by_css_selector('#id_username').send_keys('xxxxxxxxx')
    # driver.find_element_by_css_selector('input#id_username').send_keys('xxxxxxxxx')

    # class
    # driver.find_element_by_css_selector('.form-control').send_keys('xxxxxxxxxxx')
    # driver.find_element_by_css_selector('input.form-control').send_keys('xxxxxxxxxxx')

    # tag name
    # print(driver.find_element_by_css_selector('input').get_attribute('name'))

    # 通配符 ^  以什么开头
    # driver.find_element_by_css_selector('input[id=id_username]').send_keys('xxxxxxxxx')
    # driver.find_element_by_css_selector('input[id ^=id_pas]').send_keys('xxxxxxxxx')  # 匹配以 id_pas 开头的id值，

    # 通配符 $  以什么结尾
    # driver.find_element_by_css_selector('input[id $=word]').send_keys('xxxxxxxxx')  #

    # 通配符 * 包含
    # driver.find_element_by_css_selector('input[id *=pass]').send_keys('xxxxxxxxx')

    # ----------------------------------- by 选择器 ---------------------

    # driver.find_element(By.ID, 'id_username').send_keys('xxxxxxxxxxxxxxxxxxxx')
    By.XPATH
    By.LINK_TEXT
    By.CSS_SELECTOR
    By.CLASS_NAME
    By.TAG_NAME
    By.ID
    
except Exception as e:
    print(e)
finally:
    time.sleep(3)
    driver.quit()




