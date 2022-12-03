"""auto_port URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 项目相关
    url(r'^$', views.index, name='index'),
    url(r'^add_it/$', views.add_it, name='add_it'),
    url(r'^edit_it/(?P<pk>\d+)$', views.edit_it, name='edit_it'),
    url(r'^del_it/(?P<pk>\d+)$', views.del_it, name='del_it'),
    url(r'^upload/(?P<pk>\d+)$', views.upload, name='upload'),


    # 用例相关
    url(r'^case_list/(?P<pk>\d+)$', views.case_list, name='case_list'),
    url(r'^add_case/(?P<pk>\d+)$', views.add_case, name='add_case'),
    url(r'^edit_case/(?P<pk>\d+)/(?P<api_id>\d+)$', views.edit_case, name='edit_case'),
    url(r'^del_case/(?P<pk>\d+)/(?P<api_id>\d+)$', views.del_case, name='del_case'),

    # 执行用例
    url(r'^run_case/(?P<pk>\d+)/(?P<api_id>\d+)$', views.run_case, name='run_case'),
    # 下载用例报告
    url(r'^download_case_report/(?P<pk>\d+)/(?P<api_id>\d+)$', views.download_case_report, name='download_case_report'),

    # 日志相关
    url(r'^logs/list/$', views.logs_list, name='logs_list'),
    url(r'^logs/preview/(?P<logs_id>\d+)$', views.logs_preview, name='logs_preview'),

    # 可视化
    url(r'^echarts_show/$', views.echarts_show, name='echarts_show'),

    # 发邮件
    url(r'^send_email/$', views.send_email, name='send_email'),
]
