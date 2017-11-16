from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators import csrf
from . import exw
import pythoncom
import xlwings as xw
import MySQLdb
db = MySQLdb.connect(host="localhost", user="root", passwd="", db="EIA",charset = "utf8")
c = db.cursor()
def products_submit(request):
    if request.POST:
        formdict = request.POST.dict()
        list_p = []
        list_m = []
        list_e = []
        for key in formdict:
            if(str(key).find('p')!=-1):
                list_p.append(formdict[key])
            if (str(key).find('M') != -1):
                list_m.append(formdict[key])
            if (str(key).find('E') != -1):
                list_e.append(formdict[key])
        print(list_p)
        print(list_m)
        print(list_e)
        ProductsToSQL(list_p)
        MaterialsToSQL(list_m)
        EquipsToSQL(list_e)
        return HttpResponse("submit success")
def ProductsToSQL(list):
    str2 = ""
    counter = 0
    str1 = "INSERT INTO eia_products (productsName,num,unit,remark,enterpriseId_id) VALUES ("
    str2 = str1
    for info in list:
        if(counter==0 and info == ""): break;
        counter = counter + 1
        str2 += "'" + info + "',"
        if (counter == 4):
            counter = 0;
            str2 += "'0')"
            print(str2)
            try:
                c.execute(str2)
                db.commit()
                r = c.fetchone()
                print(r)
            except:
                db.rollback()
            str2 = str1
def MaterialsToSQL(list):
    str2 = ""
    counter = 0
    str1 = "INSERT INTO eia_materials (materialName,num,unit,isOffcut,state,enterpriseId_id) VALUES ("
    str2 = str1
    for info in list:
        if(counter==0 and info == ""): break;
        counter = counter + 1
        str2 += "'" + info + "',"
        if (counter == 5):
            counter = 0;
            str2 += "'0')"
            print(str2)
            try:
                c.execute(str2)
                db.commit()
                r = c.fetchone()
                print(r)
            except:
                db.rollback()
            str2 = str1
def EquipsToSQL(list):
    str2 = ""
    counter = 0
    str1 = "INSERT INTO eia_equipments (equipName,num,unit,remark,enterpriseId_ID) VALUES ("
    str2 = str1
    for info in list:
        if(counter==0 and info == ""): break;
        counter = counter + 1
        str2 += "'" + info + "',"
        if (counter == 4):
            counter = 0;
            str2 += "'0')"
            print(str2)
            try:
                c.execute(str2)
                db.commit()
                r = c.fetchone()
                print(r)
            except:
                db.rollback()
            str2 = str1





