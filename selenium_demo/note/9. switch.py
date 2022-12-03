# -*- coding: utf-8 -*-
# @Time    : 2020/5/12 16:21
# @Author  : 张开
# File      : 9. switch.py


# import time
# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait  # 等待页面加载某些元素
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By

# 获取driver
# driver = webdriver.Chrome()
# driver.implicitly_wait(20)
#
# try:
    # # 发请求
    # driver.get('https://www.baidu.com')
    #
    # # 定位标签并输入值然后点击
    # driver.find_element_by_id('kw').send_keys('听雨危楼-cnblogs')
    # time.sleep(1)
    # driver.find_element_by_id('su').click()
    #
    # # 在新窗口中，点击结果标签
    # wait.until(EC.presence_of_element_located((By.LINK_TEXT, '听雨危楼 - 博客园'))).click()
    # # driver.find_element_by_link_text('听雨危楼').click()

    # 所有打开的窗口都存在这个数组中
    # print(driver.window_handles)  # ['CDwindow-922052E58B50E4A32401C904D478CC8E', 'CDwindow-AC58D7837A577C8878BE283F554B0E52', 'CDwindow-8196C4B6F2DEAAD7F0AF10DA17BC44ED']

    # 根据数组下标索引切换窗口
    # time.sleep(3)
    # driver.switch_to.window(driver.window_handles[1])
    # time.sleep(3)
    # driver.switch_to.window(driver.window_handles[0])


    # 切换 iframe
    # driver.get('https://email.163.com/')
    # div = driver.find_element_by_id('urs163Area')
    # iframe = div.find_element_by_tag_name('iframe')
    # driver.switch_to.frame(iframe)
    # driver.find_element_by_name('email').send_keys('xxxxxxxxxxxxxxxxxxxxxxxxx')
    #
    #
    #
    # driver.switch_to.default_content()
    # driver.switch_to.alert
    # # driver.switch_to_window()   # 表示，该方法，现在还能凑活用，但是即将(甚至已经在新版本中弃用)被弃用，由别的方法代替
    # driver.switch_to.window()


#     driver.get('https://jqueryui.com/droppable/')
#     driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
#
#     t1 = driver.find_element_by_id('draggable')
#     t2 = driver.find_element_by_id('droppable')
#     from selenium.webdriver import ActionChains
#     ActionChains(driver).drag_and_drop(t1, t2).perform()
#     time.sleep(2)
#     driver.switch_to.default_content()
#     driver.find_element_by_link_text('jQuery UI').click()
#
#
# finally:
#     # 关闭浏览器
#     time.sleep(3)
#     driver.quit()
#     # 截止2019-6-11，代码无误

























