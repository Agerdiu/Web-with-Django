from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from .form import EnterpriseForm,UserLoginForm,UserRegisterForm
from django.contrib import auth
from .models import User,Enterprise
from django.utils import timezone


def index(request):
    return render(request, 'EIA/index.html', context={
        'title': 'index',
        'welcome': 'welcome to index'
    })


def register(request):
    if request.POST:
        formdict = request.POST.dict()
        print(formdict)
        f=UserRegisterForm(request.POST)
        if f.is_valid():
            first_name=f.cleaned_data['first_name']
            telephone=f.cleaned_data['telephone']
            email=f.cleaned_data['email']
            password=f.cleaned_data['password']
            is_manager=f.cleaned_data['is_manager']
            environmentAssessmentCompany = f.cleaned_data['environmentAssessmentCompany']
            userName = email
            user = User.objects.filter(username__exact=userName, email__exact=email)
            if user:
                return render(request, 'EIA/register.html', context={'error': '账户已存在，请更换邮箱'})
            else:
                user=User(username=userName,email=email,telephone=telephone,password=password,first_name=first_name,is_manager=is_manager,environmentAssessmentCompany=environmentAssessmentCompany)
                user.set_password(password)
                user.save()
                return render(request, 'EIA/gis.html', context={})
        else:
            return render(request, 'EIA/register.html', context={'error': '输入不合法，请重新输入'})
    else:
        return render(request, 'EIA/register.html', context={})


def login(request):
    if request.POST:
        f = UserLoginForm(request.POST)
        if f.is_valid():
            email=f.cleaned_data['email']
            password=f.cleaned_data['password']
            userName=email
            user = auth.authenticate(username=userName, password=password)
            if user:
                auth.login(request, user)
                now_time = timezone.now()
                user.last_login = now_time
                user.save()
                return redirect('/gis')
            else:
                return render(request, 'EIA/login.html', context={'error': '账户或密码错误，不存在，请重新输入'})
        else:
            return render(request, 'EIA/login.html', context={'error': '账户或密码错误，不存在，请重新输入'})
    else:
        return render(request, 'EIA/login.html', context={})



def gis(request):
    user = request.user
    if request.user.is_authenticated():
        enterprise_list=user.enterprise_set.all()
        for enterprise in enterprise_list:
            enterprise.durationTime=timezone.now()-enterprise.createTime
        return render(request, 'EIA/gis.html', context={'enterprise_list':enterprise_list,'check':123})
    else:
        return render(request, 'EIA/gis.html', context={})





def table(request):
    return render(request, 'EIA/table.html', context={})

def products(request):
    return render(request, 'EIA/products.html', context={})


def download(request,enterpriseId):
    enterprise=post = get_object_or_404(Enterprise, enterpriseId=enterpriseId)
    print(enterpriseId)
    return HttpResponse("good")

def upload(request,enterpriseId):
    enterprise=post = get_object_or_404(Enterprise, enterpriseId=enterpriseId)
    print(enterpriseId)
    return HttpResponse("good")