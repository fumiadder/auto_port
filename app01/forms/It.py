from django.forms import ModelForm
from app01 import models

from app01.forms.bootstrap import BootStrapModelForm


class ItModelForm(BootStrapModelForm, ModelForm):
    bootstrap_exclude_list = ['start_time', 'end_time']

    class Meta:
        model = models.It
        fields = '__all__'
        widgets = {}
