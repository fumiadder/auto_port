from django.forms import ModelForm
from django.forms import widgets as wid
from django import forms
from app01 import models

from app01.forms.bootstrap import BootStrapModelForm


class ItModelForm(BootStrapModelForm, ModelForm):
    bootstrap_exclude_list = ['start_time', 'end_time']
    start_time = forms.DateField(label='项目开始时间', widget=wid.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}))
    end_time = forms.DateField(label='项目结束时间', widget=wid.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}))

    class Meta:
        model = models.It
        fields = '__all__'
