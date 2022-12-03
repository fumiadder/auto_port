import json
import xlrd
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
from django.http import FileResponse
from django.utils.encoding import escape_uri_path  # 导入这个家伙解决中文显示问题

from app01.forms.It import ItModelForm
from app01.forms.case import CaseModelForm
from app01 import models
from utils import RequestHand


# Create your views here.


def index(request):
    """首页"""
    it_obj_list = models.It.objects.all()
    return render(request, 'index.html', {'it_obj_list': it_obj_list})


def add_it(request):
    """添加项目"""
    if request.method == 'GET':
        form = ItModelForm()
        return render(request, 'change_It.html', {'form': form})
    form = ItModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'change_It.html', {'form': form})


def edit_it(request, pk):
    """编辑项目"""
    it_obj = models.It.objects.filter(pk=pk).first()
    if request.method == 'GET':
        form = ItModelForm(instance=it_obj)
        return render(request, 'change_It.html', {'form': form, 'flag': True})
    form = ItModelForm(data=request.POST, instance=it_obj)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'change_It.html', {'form': form})


def del_it(request, pk):
    """删除项目"""
    models.It.objects.filter(pk=pk).delete()
    return redirect('index')


def case_list(request, pk):
    """用例列表"""
    it_obj = models.It.objects.filter(pk=pk).first()
    api_list = models.Api.objects.filter(api_sub_it=it_obj)
    return render(request, 'case_list.html', {'it_obj': it_obj, 'api_list': api_list})


def add_case(request, pk):
    """添加用例"""
    it_obj = models.It.objects.filter(pk=pk).first()
    if request.method == "GET":
        form = CaseModelForm()
        return render(request, 'change_case.html', {"form": form, 'it_obj': it_obj})
    form = CaseModelForm(data=request.POST)
    if form.is_valid():
        form.instance.api_sub_it = it_obj
        form.save()
        return redirect('case_list', pk=it_obj.id)
    return render(request, 'change_case.html', {'form': form, 'it_obj': it_obj})


def edit_case(request, pk, api_id):
    """ 编辑用例 """
    it_obj = models.It.objects.filter(pk=pk).first()
    api_obj = models.Api.objects.filter(id=api_id).first()
    if request.method == "GET":
        form = CaseModelForm(instance=api_obj)
        return render(request, 'change_case.html', {"form": form, 'it_obj': it_obj})
    form = CaseModelForm(data=request.POST, instance=api_obj)
    if form.is_valid():
        # 编辑时将状态改为未执行状态
        # print(form.instance.__dict__)
        form.instance.__dict__['api_pass_status'] = 0
        form.instance.__dict__['api_run_status'] = 0
        form.instance.__dict__['api_report'] = ''

        form.instance.api_sub_it = it_obj
        form.save()
        return redirect('case_list', pk=it_obj.id)
    return render(request, 'change_case.html', {'form': form, 'it_obj': it_obj})


def del_case(request, pk, api_id):
    """删除用例"""
    it_obj = models.It.objects.filter(pk=pk).first()
    models.Api.objects.filter(id=api_id).delete()
    return redirect('case_list', pk=it_obj.id)


@csrf_exempt
def run_case(request, pk, api_id=0):
    """执行用例, 都遵循一套逻辑"""
    if request.is_ajax():
        # 批量执行用例
        api_id_list = request.POST.get('api_id_list')
        # print(api_id_list, type(api_id_list))    # ["4","5"] <class 'str'>
        api_id_list = json.loads(api_id_list)
        api_obj_list = models.Api.objects.filter(pk__in=api_id_list)
        RequestHand.run_case(api_obj_list)
        return JsonResponse({'path': '/logs/list/'})

    # 单个执行
    # it_obj = models.It.objects.filter(pk=pk).first()
    api_obj = models.Api.objects.filter(id=api_id).first()
    RequestHand.run_case([api_obj])  # 单个用例也用批量执行的逻辑来

    return redirect('logs_list')


def download_case_report(request, pk, api_id):
    """下载测试报告"""

    api_obj = models.Api.objects.filter(id=api_id).first()
    response = FileResponse(api_obj.api_report)
    response['Content-Type'] = 'application/octet-stream'
    # response['Content-Disposition'] = 'attachment;filename="{}.py"'.format(escape_uri_path("我是中文啦"))
    response['Content-Disposition'] = 'attachment;filename="{}.{}"'.format(escape_uri_path(api_obj.api_name), 'html')
    return response


def logs_list(request):
    """日志主页"""
    logs_obj_list = models.Logs.objects.all()
    return render(request, 'logs_list.html', {'logs_obj_list': logs_obj_list})


def logs_preview(request, logs_id):
    """预览日志"""
    log_obj = models.Logs.objects.filter(id=logs_id).first()

    if request.method == 'POST':
        """日志下载"""
        response = FileResponse(log_obj.log_report)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{}.{}"'.format(escape_uri_path(log_obj.log_sub_it.name),
                                                                               'html')
        return response
    return render(request, 'logs_preview.html', {'log_obj': log_obj})


from utils.EchartsHand import EchartsHandler


@csrf_exempt
def echarts_show(request):
    """可视化"""
    if request.is_ajax():
        data_dict = {}
        data_dict.update(EchartsHandler().pie())
        data_dict.update(EchartsHandler().line_race())
        return JsonResponse({'status': True, 'data_dict': data_dict})
    return render(request, 'echarts_show.html')


from django.shortcuts import render, HttpResponse
from django.core.mail import EmailMessage


def send_email(request):
    """发送带附件的邮件"""
    msg = EmailMessage(
        subject='这是带附件的邮件标题',
        body='这是带附件的邮件内容',
        from_email=settings.EMAIL_HOST_USER,  # 也可以从settings中获取
        to=settings.EMAIL_TO_USER_LIST
    )
    msg.attach_file('d:\data\\1045699\Pictures\Screenshots\haha.png')
    msg.send(fail_silently=False)
    return HttpResponse('OK')


from django.db import transaction


def upload(request, pk):
    """上传文件"""
    if request.is_ajax():
        try:
            with transaction.atomic():
                file_obj = request.FILES.get("f1")
                it_obj_pk = request.POST.get("it_obj_pk")
                # print(it_obj_pk, file_obj)  # 6 接口测试示例-2.xlsx
                book_obj = xlrd.open_workbook(filename=None, file_contents=file_obj.read())
                sheet = book_obj.sheet_by_index(0)
                title = sheet.row_values(0)
                data_list = [dict(zip(title, sheet.row_values(item))) for item in range(1, sheet.nrows)]
                """
                [
                    {
                        'case_num': 'neeo_001', 
                        'title': '下单接口', 
                        'desc': 'neeo项目的下单接口', 
                        'url': 'http://www.neeo.cc:6002/pinter/com/buy', 
                        'method': 'post', 
                        'params': '', 
                        'data': '{"param":{"skuId":123,"num":10}}', 
                        'json': '', 
                        'cookies': '', 
                        'headers': '', 
                        'except': '{"code": "0", "message": "success"}'
                    }
                ]
                """
                for item in data_list:
                    models.Api.objects.create(
                        api_sub_it_id=it_obj_pk,
                        api_name=item['title'],
                        api_desc=item['desc'],
                        api_url=item['url'],
                        api_method=item['method'],
                        api_params=item['params'],
                        api_data=item['data']
                    )
            return JsonResponse({"status": 200, 'path': '/list_api/{}'.format(pk)})
        except Exception as e:
            return JsonResponse({
                "status": 500,
                'path': '/list_api/{}'.format(pk),
                "it_obj_pk": pk,
                "errors": "这里只能上传 [xls] or [xlsx] 类型的表格，并且表格的字段要符合要求， 错误详情:{}".format(e)
            })
    else:
        return render(request, 'upload.html', {'it_obj_pk': pk})
