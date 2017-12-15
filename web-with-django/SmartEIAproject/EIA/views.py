from django.http import HttpResponse
from django.shortcuts import render,redirect
from .form import EnterpriseForm,UserLoginForm,UserRegisterForm,ProductForm,EquipmentForm,MaterialForm,EnterpriseUpdateForm,EnterpriseUpdate_Worker,ChangeInfoForm,EnterpriseUpdate_Agency
from django.contrib import auth
from .models import User,Enterprise
from django.utils import timezone
import os
from django.http import StreamingHttpResponse
from django.http import QueryDict
from .excel_write import enterpriseExcelWrite,equipmentExcelWrite,productExcelWrite,materialExcelWrite,Excelcreate,getfileextension
from django.forms import formset_factory
from django.urls import reverse

def index(request):
    return redirect("/manage")


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
            position=f.cleaned_data['position']
            environmentAssessmentCompany = f.cleaned_data['environmentAssessmentCompany']
            userName = email
            user = User.objects.filter(username__exact=userName, email__exact=email)
            if user:
                return render(request, 'EIA/register.html', context={'error': '账户已存在，请更换邮箱'})
            else:
                user=User(username=userName,email=email,telephone=telephone,password=password,first_name=first_name,position=position,environmentAssessmentCompany=environmentAssessmentCompany)
                user.set_password(password)
                user.save()
                user.manager = user
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
                    return redirect("/workerManage")
                else:
                    return redirect("/index")
            else:
                return render(request, 'EIA/login.html', context={'error': '账户或密码错误，不存在，请重新输入'})
        else:
            return render(request, 'EIA/login.html', context={'error': '账户或密码错误，不存在，请重新输入'})
    else:
        return render(request, 'EIA/login.html', context={})


def logout(request):
    auth.logout(request)
    return render(request, 'EIA/login.html', context={})



def workerManage(request):
    user = request.user
    if user.is_authenticated():
        enterprise_list=user.workEnterprise.all()
        for enterprise in enterprise_list:
            enterprise.durationTime=timezone.now()-enterprise.createTime
        if user.manager!=user:
            manager=user.manager
        else:
            manager=None
        return render(request, 'EIA/workerManage.html', context={'enterprise_list':enterprise_list,'manager':manager})
    else:
        return render(request, 'EIA/login.html', context={})


def managerManage(request):
    user=request.user
    if user.is_authenticated():
        worker_list=User.objects.filter(manager=user)
        enterprise_list=Enterprise.objects.none()
        for worker in worker_list:
            enterprise_list= worker.workEnterprise.all()|enterprise_list
        for enterprise in enterprise_list:
            enterprise.durationTime=timezone.now()-enterprise.createTime
        agency_list=User.objects.filter(position='AC')###获取所有中介

        return render(request, 'EIA/managerManage.html', context={'enterprise_list': enterprise_list,'agency_list':agency_list})
    else:
        return render(request, 'EIA/login.html', context={})


def agencyManage(request):
    user = request.user
    if user.is_authenticated():
        enterprise_list=user.agencyEnterprise.all()
        for enterprise in enterprise_list:
            enterprise.durationTime=timezone.now()-enterprise.createTime
        return render(request, 'EIA/agencyManage.html', context={'enterprise_list':enterprise_list})
    else:
        return render(request, 'EIA/login.html', context={})



def updateStateType(request):
    if request.POST:
        IDlist = request.POST.getlist("enterpriseId")
        if (request.user.position == "WK"):
            Typelist = request.POST.getlist("projectType")
            Statelist = request.POST.getlist("projectState")
            WriterRemarklist = request.POST.getlist("writerRemark")
            Intermediary = request.POST.getlist("intermediarySourcesCompleted")
            i = 0
            while (i < len(IDlist)):
                Q = QueryDict("enterpriseId=" + IDlist[i] + "&writerRemark=" + WriterRemarklist[i] + "&projectType=" + Typelist[
                    i] + "&projectState=" + Statelist[i] + "&intermediarySourcesCompleted=" + Intermediary[i])
                print(Q)
                i = i + 1
                f = EnterpriseUpdate_Worker(Q)
                if f.is_valid():
                    enterpriseId = f.cleaned_data['enterpriseId']
                    enterprise = Enterprise.objects.get(enterpriseId=enterpriseId)
                    enterprise.projectType = f.cleaned_data['projectType']
                    enterprise.projectState = f.cleaned_data['projectState']
                    enterprise.writerRemark = f.cleaned_data['writerRemark']
                    enterprise.intermediarySourcesCompleted = f.cleaned_data['intermediarySourcesCompleted']
                    enterprise.save()
                else:
                    HttpResponse("error")
            return redirect("/workerManage")
        if (request.user.position == "AC"):
            IntermediaryRemarklist = request.POST.getlist("intermediaryRemark")
            i = 0
            while (i < len(IDlist)):
                Q = QueryDict("enterpriseId=" + IDlist[i] + "&intermediaryRemark=" + IntermediaryRemarklist[i])
                print(Q)
                i = i + 1
                f = EnterpriseUpdate_Agency(Q)
                if f.is_valid():
                    enterpriseId = f.cleaned_data['enterpriseId']
                    enterprise = Enterprise.objects.get(enterpriseId=enterpriseId)
                    enterprise.intermediaryRemark = f.cleaned_data['intermediaryRemark']
                    enterprise.save()
                else:
                    HttpResponse("error")
            return redirect("/agencyManage")
        if(request.user.position=="MG"):
            Typelist = request.POST.getlist("projectType")
            Statelist = request.POST.getlist("projectState")
            Agencylist = request.POST.getlist("agencyId")
            Intermediary = request.POST.getlist("intermediarySourcesCompleted")
            i = 0
            while (i < len(IDlist)):
                Q = QueryDict("enterpriseId=" + IDlist[i] + "&agencyId=" + Agencylist[i] + "&projectType=" + Typelist[
                    i] + "&projectState=" + Statelist[i] + "&intermediarySourcesCompleted=" + Intermediary[i])
                print(Q)
                i = i + 1
                f = EnterpriseUpdateForm(Q)
                if f.is_valid():
                    enterpriseId = f.cleaned_data['enterpriseId']
                    enterprise = Enterprise.objects.get(enterpriseId=enterpriseId)
                    enterprise.projectType = f.cleaned_data['projectType']
                    enterprise.projectState = f.cleaned_data['projectState']
                    enterprise.agencyId = f.cleaned_data['agencyId']
                    enterprise.intermediarySourcesCompleted = f.cleaned_data['intermediarySourcesCompleted']
                    enterprise.save()
                else:
                    HttpResponse("error")
            return redirect("/managerManage")
        return render(request, 'EIA/uploading.html', context={'enterpriseId': 1})
    else:
        return redirect("/workerManage")

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

def manage(request):
    user = request.user
    if user.is_authenticated():
        if user.position == 'MG':
            return redirect("/managerManage")
        elif user.position == 'WK':
            return redirect("/workerManage")
        elif user.position == 'WK':
            return redirect("/agencyManage")
        else:
            return render(request, 'EIA/index.html', context={})
    else:
        return render(request, 'EIA/login.html', context={})


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


def download(request,enterpriseId,target):
    exceldir = os.path.join('C:\\文件库', 'Projects', 'P' + enterpriseId)
    if(target=="base"):
        filename = os.path.join(exceldir, "基础信息表单.rar") # 要下载的文件路径
    if (target == "report"):
        filename = os.path.join(exceldir, "报告文件包.rar")  # 要下载的文件路径
    the_file_name = 'P' + enterpriseId +"_"+ target + ".rar"  # 显示在弹出对话框中的默认的下载文件名
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
        i = 1
        while(i<=11):
            file_obj = request.FILES.getlist('img'+str(i))
            j = 1
            for f in file_obj:
                if (i == 1): name = "平面布置图"+ getfileextension(f.name)
                if (i == 2): name = "工艺流程图"+ getfileextension(f.name)
                if (i == 3): name = "租赁合同" + str(j) + getfileextension(f.name)
                if (i == 4): name = "场地使用证明" + str(j) + getfileextension(f.name)
                if (i == 5): name = "营业执照" + getfileextension(f.name)
                if (i == 6): name = "身份证" + getfileextension(f.name)
                if (i == 7): name = "厂址东" + getfileextension(f.name)
                if (i == 8): name = "厂址南" + getfileextension(f.name)
                if (i == 9): name = "厂址西" + getfileextension(f.name)
                if (i == 10): name = "厂址北" + getfileextension(f.name)
                if (i == 11): name = "环保证复印件" + getfileextension(f.name)
                filename = os.path.join(filedir,name)
                if not os.path.isdir(filedir):
                    os.makedirs(filedir)
                fobj = open(filename, 'wb')
                for chrunk in f.chunks():
                    fobj.write(chrunk)
                fobj.close()
                j = j + 1
            i = i + 1
        return manage(request)
    else:
        return HttpResponse("error")

def updatefiles(request,enterpriseId):
    if request.POST:
        filedir = os.path.join('C:\\文件库', 'Projects', 'P' + str(enterpriseId))
        i = 1;
        while (i <= 2):
            if (i == 1):
                file_obj = request.FILES.getlist('base')
            if (i == 2):
                file_obj = request.FILES.getlist('report')
            for f in file_obj:
                if (i == 1): name = "基础信息表单.rar"
                if (i == 2): name = "报告文件包.rar"
                filename = os.path.join(filedir, name)
                if not os.path.isdir(filedir):
                    os.makedirs(filedir)
                fobj = open(filename, 'wb')
                for chrunk in f.chunks():
                    fobj.write(chrunk)
                fobj.close()
            i = i + 1;
        return manage(request)


def changeInfo(request):
    user=request.user
    if request.user.is_authenticated():
        if request.POST:
            f=ChangeInfoForm(request.POST)
            if f.is_valid():
                email=f.cleaned_data['email']
                print(email)
                try:
                    manager=User.objects.get(email=email)
                except User.DoesNotExist:
                    manager=None
                if manager:
                    user.manager=manager
                    user.save()
                    return redirect("/workerManage")
                else:
                    return redirect("/workerManage")
            else:
                print("error")
                return redirect("/workerManage")
        else:
            return redirect("/workerManage")
    else:
        return render(request, 'EIA/login.html', context={})