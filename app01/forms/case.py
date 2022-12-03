from django.forms import ModelForm
from app01.forms.bootstrap import BootStrapModelForm
from app01 import models


class CaseModelForm(BootStrapModelForm, ModelForm):

    class Meta:
        model = models.Api
        exclude = ['api_sub_it', 'api_report', 'api_run_time', 'api_pass_status', 'api_run_status']
