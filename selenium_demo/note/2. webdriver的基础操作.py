# -*- coding: utf-8 -*-
# @Time    : 2020/5/12 11:07
# @Author  : 张开
# File      : 2. webdriver的基础操作.py


import time
from selenium import webdriver

driver = webdriver.Chrome()


driver.get(url='http://www.neeo.cc:6005/login/')

# driver.find_element()   # 定位标签
# print(driver.title)
# driver.close()  # 关闭当前的窗口
# driver.quit()  # 退出浏览器
# print(driver.page_source)  # 获取页面的内置
# 设置浏览器的大小
# driver.set_window_size(800, 600)
# print(driver.get_window_size())  # 获取浏览器窗口大小
# driver.save_screenshot('a.png')  # 屏幕截图，保存图片的类型必须是 png
# driver.refresh()  # 刷新
# driver.back()  # 后退
# driver.forward() # 前进

# driver.get_cookies() # 获取cookies
# driver.current_url  # 获取当前window的url
# driver.current_window_handle  # 获取当前窗口对象
# driver.execute_script("alert('xxoo');")  # 执行 js代码

# 常用的选择器

# driver.find_element_by_id('')
# driver.find_elements_by_id()
# driver.find_element_by_class_name()
# driver.find_elements_by_class_name()
# driver.find_element_by_name()
# driver.find_elements_by_name()
# driver.find_element_by_tag_name()
# driver.find_elements_by_tag_name()

# 如果以上方式定位失败，会报错：NoSuchElementException
# 拿到标签对象之后我们能干什么？
try:
    # 获取标签对象
    # input_obj = driver.find_element_by_id("id_username")
    # print(input_obj)
    # 获取标签的内容
    # title = driver.find_element_by_class_name('title')
    # print(title.text)

    # 为input框填写值
    driver.find_element_by_id("id_username").send_keys('张开最帅啦')
    # 获取input框的值
    input_obj  = driver.find_element_by_id('id_username')
    print(input_obj.get_attribute('value'))
    driver.maximize_window()  # 窗口最大化
    # 清空值
    time.sleep(2)
    input_obj.clear()
    driver.minimize_window()  # 窗口最小化
    # 获取input框的属性
    print(input_obj.get_attribute('class'))
    print(input_obj.get_property('name'))
    # 获取标签的css样式
    print(input_obj.value_of_css_property('color'))

    # 获取标签中的子标签
    div_obj = driver.find_element_by_class_name('col-xs-3')
    div_obj.find_element_by_tag_name('input').submit()

    # 获取验证码图片的大小
    print(driver.find_element_by_id('imageCode').size)

except Exception as e:
    print(e)

finally:
    time.sleep(3)
    driver.quit()










































