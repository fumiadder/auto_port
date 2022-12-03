import os
import django
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

# 准备工作
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "auto_port.settings")
django.setup()

# 一定得在准备工作之后才能导入相关模块
from app01 import models
from utils.RequestHand import run_case


def job1():
    # print('job1', datetime.datetime.now())
    api_obj_list = models.It.objects.all()
    # print(api_obj_list)  # <QuerySet [<It: x1>, <It: x2>]>
    for api_obj in api_obj_list:
        if datetime.date.today() == api_obj.end_time:
            run_case(api_obj.api_set.all())


def run():
    scheduler = BlockingScheduler()
    scheduler.add_job(job1, 'interval', seconds=10, id='job1')  # 每隔10秒执行一次
    scheduler.start()


if __name__ == '__main__':
    job1()
