from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'EIA/index.html', context={
        'title': 'index',
        'welcome': 'welcome to index'
    })


def login(request):
    return render(request, 'EIA/login.html', context={})


def register(request):
    return render(request, 'EIA/register.html', context={})

def table(request):
    return render(request, 'EIA/table.html', context={})