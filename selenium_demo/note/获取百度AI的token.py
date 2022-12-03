# -*- coding: utf-8 -*-
# @Time    : 2020/5/12 17:12
# @Author  : 张开
# File      : 获取百度AI的token.py


import requests
import base64
# # client_id 为官网获取的AK， client_secret 为官网获取的SK
# host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=SBHMsV1cYBeOXSAL0X975GCG&client_secret=LedXa2pPqKT9WmO2qU1FegDg9u2Gbe27'
# response = requests.get(host)
# if response:
#     access_token = response.json()['access_token']






'''
通用文字识别
'''

request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
# 二进制方式打开图片文件
f = open(r'D:\video\s28-testing-day18-selenium\note\b.png', 'rb')
img = base64.b64encode(f.read())

params = {"image": img}
access_token = '24.83c36a5a583d87923919104793022a56.2592000.1591866873.282335-19847256'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print(response.json()['words_result'][0]['words'])