# -*- coding: utf-8 -*-
# @Time    : 2020/5/12 16:42
# @Author  : 张开
# File      : 10. 截图.py


from PIL import Image
from selenium import webdriver

full_img = './a.png'
code_img = './b.png'

# driver = webdriver.Chrome()
# driver.implicitly_wait(10)

# driver.get('http://www.neeo.cc:6005/login/')
# driver.save_screenshot(full_img)
#
# # 获取验证码的大小
# imageCode = driver.find_element_by_id('imageCode')
# print(imageCode.size)
# left = imageCode.location['x'] * 1.24
# top = imageCode.location['y'] * 1.24
# right = imageCode.size['width'] + left
# height = imageCode.size['height'] + top
# temp = Image.open(full_img)
# temp = temp.crop((left, top, right, height))
# temp.save(code_img)
#
# import time
# time.sleep(5)
# driver.quit()


# imageCode = driver.find_element_by_id('imageCode')
# imageCode.screenshot(code_img)
#
#
# import time
# time.sleep(5)
# driver.quit()

# def get_img():
#
#     driver = webdriver.PhantomJS(executable_path=r"C:\Python36\Scripts\phantomjs-2.1.1-windows\bin\phantomjs.exe")
#     driver.implicitly_wait(time_to_wait=10)
#     driver.get('http://www.neeo.cc:6005/index/')
#     # 设置视图大小
#     # driver.viewportSize = driver.get_window_size()
#     driver.save_screenshot('a.png')
#     driver.quit()
#
# if __name__ == '__main__':
#     get_img()
#

# ---------------------------- 实战 ----------------------------

import base64
import requests
import unittest
from selenium import webdriver
from HTMLTestRunnerSelenium import HTMLTestRunner



class MyCase(unittest.TestCase):
    user = "18211101742"
    password = "root1234"
    code_img = r'D:\video\s28-testing-day18-selenium\note\c.png'

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    def setUp(self):
        self.driver.get('http://www.neeo.cc:6005/login/')


    def test_case_01(self):

        self.driver.find_element_by_id('id_username').send_keys(self.user)
        self.driver.find_element_by_id('id_password').send_keys(self.password)

        # 首先获取验证码图片，然后调用百度AI的文字识别接口，接着将验证码图片发送到百度服务器，得到验证码的识别结果，然后将结果send到 input 框中

        # 获取img图片
        self.driver.find_element_by_id("imageCode").screenshot(self.code_img)
        # 将图片发送到百度ai的文字识别接口
        self.driver.find_element_by_id('id_code').send_keys(self.foo())

        # 点击确定
        self.driver.find_element_by_css_selector('input[type=submit]').click()
        try:
            text = self.driver.find_element_by_class_name('col-xs-7').find_element_by_tag_name('span').text
            if text:
                # 访问失败
                self.assertEqual('', '验证码输入错误')
            else:
                pass
        except Exception:
            pass

    def test_case_02(self):
        self.driver.find_element_by_id('id_username').send_keys(self.user)
        self.driver.find_element_by_id('id_password').send_keys(self.password)

        # 首先获取验证码图片，然后调用百度AI的文字识别接口，接着将验证码图片发送到百度服务器，得到验证码的识别结果，然后将结果send到 input 框中

        self.driver.find_element_by_id('id_code').send_keys("xxxxxxxx")

        # 点击确定
        self.driver.find_element_by_css_selector('input[type=submit]').click()

        try:
            text = self.driver.find_element_by_class_name('col-xs-7').find_element_by_tag_name('span').text
            if text:
                # 访问失败
                self.assertEqual('', '验证码输入错误')
            else:
                pass
        except Exception:
            self.assertEqual('', '验证码输入错误')
    def foo(self):
        request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
        # 二进制方式打开图片文件
        f = open(self.code_img, 'rb')
        img = base64.b64encode(f.read())

        params = {"image": img}
        access_token = '24.83c36a5a583d87923919104793022a56.2592000.1591866873.282335-19847256'
        request_url = request_url + "?access_token=" + access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            return response.json()['words_result'][0]['words']
        else:
            return ''

if __name__ == '__main__':

    suite = unittest.makeSuite(testCaseClass=MyCase)
    f = open('./report.html', 'wb')
    HTMLTestRunner(verbosity=2, title='xxxx', description='ooooo', stream=f).run(suite)

    f.close()



















