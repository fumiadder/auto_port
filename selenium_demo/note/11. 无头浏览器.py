# -*- coding: utf-8 -*-
# @Time    : 2020/5/12 17:55
# @Author  : 张开
# File      : 11. 无头浏览器.py


# from selenium import webdriver
#
# def foo():
#     """
#     如果报如下错误：
#     selenium.common.exceptions.WebDriverException: Message: 'phantomjs' executable needs to be in PATH.
#     原因是在执行时，没有在 path中找到驱动，这里的解决办法是实例化driver对象时，添加executable_path参数，引用驱动的绝对路径
#     """
#
#     driver = webdriver.PhantomJS(executable_path=r"C:\Python36\Scripts\phantomjs-2.1.1-windows\bin\phantomjs.exe") # 解决如上报错
#     driver.implicitly_wait(time_to_wait=10)
#     driver.get('https://www.baidu.com')
#     print(driver.title)  # 百度一下，你就知道
#     driver.quit()
#
# if __name__ == '__main__':
#     foo()





# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# # 创建一个参数对象，用来控制chrome以无界面模式打开
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
#
# # 创建浏览器对象
# driver = webdriver.Chrome(chrome_options=chrome_options)
# # driver = webdriver.Chrome()  # 不加 chrome_options 参数就是正常的打开一个浏览器，进行操作
# driver.implicitly_wait(10)
#
# # 访问URL
# driver.get('https://www.baidu.com')
# print(driver.title)  # 百度一下，你就知道
# driver.quit()





from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# 创建浏览器对象
options = Options()
options.add_argument("-headless")
driver = webdriver.Firefox(firefox_options=options)
# driver = webdriver.Firefox()  # # 不加 firefox_options 参数就是正常的打开一个浏览器，进行操作
driver.implicitly_wait(10)

# 访问URL
driver.get('https://www.baidu.com')
print(driver.title)  # 百度一下，你就知道
driver.quit()