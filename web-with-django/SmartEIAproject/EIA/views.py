from django.http import HttpResponse
from django.shortcuts import render,redirect
from .form import EnterpriseForm,UserLoginForm,UserRegisterForm,ProductForm,EquipmentForm,MaterialForm,EnterpriseUpdateForm
from django.contrib import auth
from .models import User,Enterprise
from django.utils import timezone
import os
from django.http import StreamingHttpResponse
from django.http import QueryDict
from .excel_write import enterpriseExcelWrite,equipmentExcelWrite,productExcelWrite,materialExcelWrite,Excelcreate
from django.forms import formset_factory
from django.urls import reverse


def index(request):
    user = request.user
    if user.is_authenticated():
        return render(request, 'EIA/index.html', context={})
    else:
        return render(request, 'EIA/login.html', context={})


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
                return render(request, 'EIA/login.html', context={})
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
                request.session["userName"] = user.first_name
                print(user.first_name)
                now_time = timezone.now()
                user.last_login = now_time
                user.save()
                if(user.is_superuser==1):
                    return redirect("/manage")
                else:
                    return redirect("/gis")
            else:
                return render(request, 'EIA/login.html', context={'error': '账户或密码错误，不存在，请重新输入'})
        else:
            return render(request, 'EIA/login.html', context={'error': '账户或密码错误，不存在，请重新输入'})
    else:
        return render(request, 'EIA/login.html', context={})


def logout(request):
    auth.logout(request)
    return render(request, 'EIA/login.html', context={})

def gis(request):
    return render(request, 'EIA/index.html', context={})


def manage(request):
    user = request.user
    if user.is_authenticated():
        enterprise_list=user.enterprise_set.all()
        for enterprise in enterprise_list:
            enterprise.durationTime=timezone.now()-enterprise.createTime
        return render(request, 'EIA/manage.html', context={'enterprise_list':enterprise_list})
    else:
        return render(request, 'EIA/login.html', context={})

def updateStateType(request):
    if request.POST:
        IDlist= request.POST.getlist("enterpriseId")
        Typelist = request.POST.getlist("projectType")
        Statelist= request.POST.getlist("projectState")
        Intermediary = request.POST.getlist("intermediarySourcesCompleted")
        i=0
        while(i<len(IDlist)):
            Q = QueryDict("enterpriseId="+IDlist[i]+"&projectType="+Typelist[i]+"&projectState="+Statelist[i]+"&intermediarySourcesCompleted="+Intermediary[i])
            print(Q)
            i = i+1
            f = EnterpriseUpdateForm(Q)
            if f.is_valid():
                enterpriseId = f.cleaned_data['enterpriseId']
                enterprise = Enterprise.objects.get(enterpriseId=enterpriseId)
                enterprise.projectType = f.cleaned_data['projectType']
                enterprise.projectState = f.cleaned_data['projectState']
                enterprise.intermediarySourcesCompleted = f.cleaned_data['intermediarySourcesCompleted']
                enterprise.save()
            else :
                HttpResponse("error")
        return render(request, 'EIA/uploading.html', context={'enterpriseId': 1})
    else:
        return redirect("/manage")

def products(request,enterpriseId):
    if request.POST:
        productFormSet = formset_factory(ProductForm, extra=2, max_num=None)
        set = productFormSet(request.POST)
        if set.is_valid():
            enterprise=Enterprise.objects.get(enterpriseId=enterpriseId)
            for f in set:
                product = f.save(commit=False)
                product.enterpriseId=enterprise
                product.save()
                productExcelWrite(set,enterpriseId)
            return redirect(reverse("equipments",kwargs={'enterpriseId':enterpriseId}))
        else:
            return render(request, 'EIA/products.html', context={'error':'输入错误','enterpriseId':enterpriseId})

    else:
        return render(request, 'EIA/products.html', context={'enterpriseId':enterpriseId})


def materials(request,enterpriseId):
    if request.POST:
        materialFormSet = formset_factory(MaterialForm, extra=2, max_num=None)
        set = materialFormSet(request.POST)
        if set.is_valid():
            enterprise = Enterprise.objects.get(enterpriseId=enterpriseId)
            for f in set:
                material = f.save(commit=False)
                material.enterpriseId=enterprise
                material.save()
                materialExcelWrite(set,enterpriseId)
                return render(request, 'EIA/uploading.html', context={'enterpriseId': enterpriseId})
        else:
            return render(request, 'EIA/materials.html', context={'error': '输入错误','enterpriseId':enterpriseId})

    else:
        return render(request, 'EIA/materials.html', context={'enterpriseId':enterpriseId})



def equipments(request,enterpriseId):
    if request.POST:
        equipmentFormSet = formset_factory(EquipmentForm, extra=2, max_num=None)
        set = equipmentFormSet(request.POST)
        if set.is_valid():
            enterprise = Enterprise.objects.get(enterpriseId=enterpriseId)
            for f in set:
                equipment = f.save(commit=False)
                equipment.enterpriseId=enterprise
                equipment.save()
                equipmentExcelWrite(set,enterpriseId)
            return redirect(reverse("materials",kwargs={'enterpriseId':enterpriseId}))
        else:
            return render(request, 'EIA/equipments.html', context={'error': '输入错误','enterpriseId':enterpriseId})

    else:
        return render(request, 'EIA/equipments.html', context={'enterpriseId':enterpriseId})



def createGisForm(request):
    user = request.user
    if request.user.is_authenticated():
        if request.POST:
            f=EnterpriseForm(request.POST)
            if f.is_valid():
                enterprise=f.save(commit=False)
                enterprise.workerId=user
                enterprise.save()
                Excelcreate(enterprise.enterpriseId)
                enterpriseExcelWrite(enterprise)
                return redirect(reverse("products",kwargs={'enterpriseId':enterprise.enterpriseId}))
            else:
                print(f.errors)
                return render(request, 'EIA/createGis.html', context={'error': '输入不合法错误'})
        else:
            return render(request, 'EIA/createGis.html', context={})
    else:
        return render(request, 'EIA/login.html', context={})


def download(request,enterpriseId):
    exceldir = os.path.join('C:\\文件库', 'Projects', 'P' + enterpriseId)
    filename = os.path.join(exceldir, 'P' + enterpriseId + ".xlsm") # 要下载的文件路径
    the_file_name = 'P' + enterpriseId + ".xlsm"  # 显示在弹出对话框中的默认的下载文件名
    response = StreamingHttpResponse(readFile(filename))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)
    return response



def readFile(filename,chunk_size=512):
    with open(filename,'rb') as f:
        while True:
            c=f.read(chunk_size)
            if c:
                yield c
            else:
                break


def upload(request,enterpriseId):
    filedir = os.path.join('C:\\文件库', 'Projects', 'P' + str(enterpriseId))
    if request.POST:
        i = 1;
        while(i<=11):
            file_obj = request.FILES.getlist('img'+str(i))
            i = i + 1;
            for f in file_obj:
                filename = os.path.join(filedir, f.name)
                if not os.path.isdir(filedir):
                    os.makedirs(filedir)
                fobj = open(filename, 'wb')
                for chrunk in f.chunks():
                    fobj.write(chrunk)
                fobj.close()
        return HttpResponse("uploadsuccess")
    else:
        return HttpResponse("error")