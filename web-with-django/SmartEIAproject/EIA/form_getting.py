from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators import csrf
from . import exw
import pythoncom
import xlwings as xw
import MySQLdb
db = MySQLdb.connect(host="localhost", user="root", passwd="", db="EIA",charset = "utf8")
c = db.cursor()
def form_post(request):
    pythoncom.CoInitialize()
    if request.POST:
        ctx ={'Successed'}
        formdict = request.POST.dict()
        formdict ['enterpriseId'] = '00001';
        del formdict['csrfmiddlewaretoken']
        try:
            # 执行sql语句
            c.execute(create_sqls(formdict))
            # 提交到数据库执行
            db.commit()
            r = c.fetchone()
            print(r)
        except:
            # Rollback in case there is any error
            db.rollback()
        print(exw.ExcToDataSheet(db, '00000'))
        return HttpResponse("success")
def create_sqls(formdict):
    str = 'INSERT INTO eia_enterprise '
    substr1 = '( '
    substr2 = '( '
    for k in formdict:
        substr1 += k + ','
        substr2 +="'"+formdict[k]+"'"+ ','
    substr1 = substr1[0:len(substr1) - 1]
    substr1 += ' )'
    substr2 = substr2[0:len(substr2) - 1]
    substr2 += ' )'
    str += substr1 + ' ' + 'VALUES ' + substr2
    print(str)
    return str

