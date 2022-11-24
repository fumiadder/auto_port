from django.shortcuts import render, HttpResponse, redirect
from app01.forms.It import ItModelForm


# Create your views here.


def index(request):
    """首页"""
    return render(request, 'index.html')


def add_It(request):
    """添加项目"""
    if request.method == 'GET':
        form = ItModelForm()
        return render(request, 'add_It.html', {'form': form})
    form = ItModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'add_It.html', {'form': form})

