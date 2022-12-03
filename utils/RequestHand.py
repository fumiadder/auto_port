import os
import io
import datetime
import unittest
import json
import requests
from deepdiff import DeepDiff
from HTMLTestRunner import HTMLTestRunner

from django.conf import settings

from app01 import models


class MyUniCase(unittest.TestCase):

    def test_case(self):
        """用例"""
        # print(111111, DeepDiff(self.response, self.expect).get('type_changes'))  # {"root['code']": {'old_type': <class 'str'>, 'new_type': <class 'int'>, 'old_value': '0', 'new_value': 0}}
        # self._testMethodName = self.title
        self._testMethodDoc = self.desc

        # 值=类型不=  type_changes?  or 类型=值不=  values_changed？
        # {'type_changes': {"root['status']": {'old_type': <class 'str'>, 'new_type': <class 'int'>, 'old_value': '0', 'new_value': 0}}}
        # {'values_changed': {"root['status']": {'new_value': '2', 'old_value': '0'}}}
        self.assertEqual(DeepDiff(self.response, self.expect).get('values_changed'), None, msg=self.msg)


class Requesthandler(object):

    def __init__(self, api_obj, suite_list):
        self.api_obj = api_obj
        self.suite_list = suite_list

    def handler(self):
        """
        关于请求的一系列流程：
            1. 提取api_obj中的字段，使用requests发请求
                1. 对请求参数进行校验
                2. 将请求结果提取出来
            2. 使用unittest进行断言
            3. 更新数据库字段
            4. 将执行结果添加到日志表中(批量操作才开始保存日志表，即使单日志)
            5. 前端返回
        """
        # 发送请求断言并更新数据库字段
        self.send_msg()

    def send_msg(self):
        """发请求"""
        response = requests.request(
            method=self.api_obj.api_method,
            url=self.api_obj.api_url,
            data=self._check_data(),
            params=self._check_params(),
        )
        # print(response.json())  # {'code': '0', 'message': 'success', 'data': {'skuId': 1, 'skuName': 'ptest-1',
        # 'price': '733', 'stock': 864, 'brand': 'testfan'}}

        # 断言
        self.assert_msg(response)

    def assert_msg(self, response):
        """处理断言"""
        case = MyUniCase(methodName='test_case')
        case.expect = self._check_expect()
        case.response = response.json()

        # 优化测试报告显示
        case.title = self.api_obj.api_name
        case.desc = self.api_obj.api_desc
        case.msg = "自定义的错误信息: {}".format(DeepDiff(response.json(), self._check_expect()))

        # 将case添加到suite_list中为后面批量执行做准备
        self.suite_list.addTest(case)

        # 创建suite
        suite = unittest.TestSuite()
        # 将用例添加到盒子
        suite.addTest(case)
        # 使用执行器执行盒子中的用例
        runner = unittest.TextTestRunner()
        # runner.run(suite)

        # 生成测试报告
        self.get_report(suite)

    def get_report(self, suite):
        """生成单个测试报告"""
        # print(suite.countTestCases())   # 返回测试用例的个数 1

        # 报错TypeError: a bytes-like object is required, not 'str'
        # 就去源码的691行，修改为self.stream.write(output.encode('utf8'))
        f = io.BytesIO()  # 从内存中读取
        result = HTMLTestRunner.HTMLTestRunner(
            stream=f,
            verbosity=2,
            title=self.api_obj.api_name,
            description=self.api_obj.api_desc,
        ).run(suite)
        # 更新数据库字段
        self.update_api_status(result, f)

    def get_all_report(self, suite):
        """生成批量测试报告"""
        f = io.BytesIO()
        result = HTMLTestRunner.HTMLTestRunner(
            stream=f,
            verbosity=2,
            title=self.api_obj.api_name,
            description=self.api_obj.api_desc
        ).run(suite)
        self.update_log_status(result, f)

    def update_log_status(self, result, f):
        """更新日志表"""
        log_data = {'pass': 0, 'failed': 0, 'total': 0, 'errors': 0}
        for flag in result.__dict__['result']:
            if flag[0]:
                # 1表示用例未通过
                log_data['failed'] += 1
            else:
                log_data['pass'] += 1
            log_data['total'] += 1
        log_data['errors'] = result.__dict__['errors'].__len__()
        # print(log_data) # {'pass': 1, 'failed': 1, 'total': 2, 'errors': 0}
        models.Logs.objects.create(
            log_report=f.getvalue(),
            log_sub_it_id=self.api_obj.api_sub_it_id,
            log_errors_count=log_data['errors'],
            log_pass_count=log_data['pass'],
            log_failed_count=log_data['failed'],
            log_run_count=log_data['total']
        )

    def update_api_status(self, result, f):
        """
            更新数据相关字段的状态
            1. api_report
            2. api_run_time
            3. api_pass_status
            4. api_run_status
        :return:
        """
        obj = models.Api.objects.filter(id=self.api_obj.id).first()

        obj.api_report = f.getvalue()
        obj.api_run_time = datetime.datetime.now()
        obj.api_run_status = 1

        # print(result.__dict__['result'][0])
        for i in result.__dict__['result']:
            if i[0]:
                # 是1表示用例未通过
                obj.api_pass_status = 0
            else:
                # 是0表示用例通过
                obj.api_pass_status = 1
        # 统一保存
        obj.save()

    def _check_data(self):
        """校验请求的data参数"""
        if self.api_obj.api_data:
            # print(self.api_obj.api_data, type(self.api_obj.api_data))   # {"id":1} <class 'str'>
            return json.loads(self.api_obj.api_data)
        return {}

    def _check_params(self):
        """校验请求的params参数"""
        if self.api_obj.api_params:
            # print(self.api_obj.api_params, type(self.api_obj.api_params))   # {} <class 'str'>
            return json.loads(self.api_obj.api_params)
        return {}

    def _check_expect(self):
        """校验预期值"""
        if self.api_obj.api_expect:
            # print(self.api_obj.api_expect, type(self.api_obj.api_expect))  # {} <class 'str'>
            return json.loads(self.api_obj.api_expect)
        return {}


def run_case(api_obj_list):
    """批量执行"""
    # 在批量执行每一个用例之前创建一个suite_list,然后当批量执行中，处理断言功能执行每一个用例的时候，将封装好的用例对象添加到suite_list中
    # 当批量执行执行完毕后，suite_list中，包含了所有批量执行的用例，此时，在使用HTMLTestRunner去生成一个批量执行的测试报告
    suite_list = unittest.TestSuite()
    for api_obj in api_obj_list:
        Requesthandler(api_obj=api_obj, suite_list=suite_list).handler()
    # 生成多个用例的测试报告
    # print(suite_list)   # <unittest.suite.TestSuite tests=[<utils.RequestHand.MyUniCase testMethod=test_case>, <utils.RequestHand.MyUniCase testMethod=test_case>]>
    Requesthandler(api_obj=api_obj, suite_list=suite_list).get_all_report(suite_list)
