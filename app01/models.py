from django.db import models


# Create your models here.


class It(models.Model):
    """ 接口项目表 """
    name = models.CharField(verbose_name='项目名称', max_length=32)
    desc = models.TextField(verbose_name='项目描述', max_length=255)
    start_time = models.DateField(verbose_name='项目开始时间')
    end_time = models.DateField(verbose_name='项目结束时间')

    def __str__(self):
        return self.name

    def xxoo(self):
        """覆盖率： 用例通过的数量/总用例数量"""
        if self.api_set.count():
            result = self.api_set.filter(api_pass_status=1).count() / self.api_set.count() * 100
            return "%.2f%%" % result
        return '0'


class Api(models.Model):
    """ 接口用例表 """
    api_sub_it = models.ForeignKey(to='It', verbose_name='所属接口项目')
    api_name = models.CharField(max_length=32, default='', verbose_name='用例名称')
    api_desc = models.TextField(max_length=255, default='', verbose_name='用例描述')
    api_url = models.CharField(max_length=255, default='', verbose_name='请求URL')
    api_method = models.CharField(max_length=32, default='', verbose_name='请求类型')
    api_params = models.CharField(max_length=255, default={}, verbose_name='请求参数')
    api_data = models.CharField(max_length=255, default={}, verbose_name='请求data')
    api_expect = models.CharField(max_length=4196, default={}, verbose_name='预期结果')
    api_report = models.TextField(verbose_name='报告', default='')
    api_run_time = models.DateTimeField(null=True, verbose_name='执行时间')
    api_pass_status_choices = (
        (0, '未通过'),
        (1, '已通过')
    )
    api_pass_status = models.IntegerField(choices=api_pass_status_choices, verbose_name='执行是否通过', default=0)
    api_run_status_choices = (
        (0, '未执行'),
        (1, '已执行'),
    )
    api_run_status = models.IntegerField(choices=api_run_status_choices, verbose_name='是否执行', default=0)

    def __str__(self):
        return self.api_name


class Logs(models.Model):
    """ 用例执行记录
        1. 所属项目
        2. 执行时间
        3. 执行的测试报告
        4. 通过多少，失败多少，共执行了多少用例，通过率是多少
     """
    log_report = models.TextField(verbose_name='报告', default='')
    log_sub_it = models.ForeignKey(to='It', verbose_name='所属接口项目')
    log_run_time = models.DateTimeField(null=True, verbose_name='log日志产生时间', auto_now_add=True)
    log_pass_count = models.IntegerField(verbose_name='通过数量')
    log_failed_count = models.IntegerField(verbose_name='失败数量')
    log_errors_count = models.IntegerField(verbose_name='报错数量')
    log_run_count = models.IntegerField(verbose_name='执行用例总数')

    def pass_rate(self):
        """  通过率 """
        if self.log_run_count:
            result = self.log_pass_count / self.log_run_count * 100
            if result:
                return "%.f%%" % (result)
            else:
                return 0
        else:
            return 0

    class Meta:
        ordering = ['-log_run_time']
