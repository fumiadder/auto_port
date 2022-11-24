from django.db import models


# Create your models here.


class It(models.Model):
    name = models.CharField(verbose_name='项目名称', max_length=32)
    desc = models.TextField(verbose_name='项目描述', max_length=255)
    start_time = models.DateField(verbose_name='项目开始时间')
    end_time = models.DateField(verbose_name='项目结束时间')

    def __str__(self):
        return self.name
