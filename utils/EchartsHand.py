"""
处理数据可视化从后端获取动态数据

"""
import os
import django
import datetime


# 准备工作
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "auto_port.settings")
django.setup()


from app01 import models


class EchartsHandler(object):

    def pie(self):
        """
        饼图
        :return:
        """
        data_dict = {
            "pass_pie": {
                'title': ['通过', '失败'],
                'data': [
                    {'value': 0, 'name': '通过'},
                    {'value': 0, 'name': '失败'},
                ]
            },
            "execute_pie": {
                'title': ['已执行', '未执行'],
                'data': [
                    {'value': 0, 'name': '已执行'},
                    {'value': 0, 'name': '未执行'},
                ]
            },
        }

        it_obj_list = models.It.objects.all()
        for it_obj in it_obj_list:
            data_dict["pass_pie"]["data"][0]["value"] += it_obj.api_set.filter(api_pass_status=1).count()
            data_dict["pass_pie"]["data"][1]["value"] += it_obj.api_set.filter(api_pass_status=0).count()
            data_dict["execute_pie"]["data"][0]["value"] += it_obj.api_set.filter(api_run_status=1).count()
            data_dict["execute_pie"]["data"][1]["value"] += it_obj.api_set.filter(api_run_status=0).count()
        # print(data_dict)
        return data_dict

    def line_race(self):
        """
        折线图
        近一年，统计每个月的用例数据走势图（21年5月11号~22年5月11号） 根据 it_start_time 进行过滤
        :return:
        """
        data_dict = {
            "line_race": {
                'title': [],
                'data': []
            },
        }
        end_time = datetime.date.today()    # 2022-11-29
        start_time = end_time - datetime.timedelta(days=365)    # 2021-11-29
        it_obj = models.It.objects.filter(start_time__range=(start_time, end_time))

        X = {}  # x轴表时间段
        for item in it_obj:
            time = item.start_time.strftime('%Y-%m')
            if X.get(time):
                # 若该月份存在则用例数相加
                X[time] += item.api_set.count()
            else:
                # 若该月份不存在则直接
                X[time] = item.api_set.count()
        # print(X.items())    # dict_items([('2021-12', 2), ('2022-11', 3)])

        # 给时间排序对应其用例数
        new_data = sorted(X.items(), key=lambda x: x[0])   # [('2021-12', 2), ('2022-11', 3)]
        for data in new_data:
            data_dict["line_race"]['title'].append(data[0])
            data_dict["line_race"]['data'].append(data[1])
        # print(data_dict)    # {'line_race': {'title': ['2021-12', '2022-11'], 'data': [2, 3]}}
        return data_dict


if __name__ == '__main__':
    EchartsHandler().line_race()