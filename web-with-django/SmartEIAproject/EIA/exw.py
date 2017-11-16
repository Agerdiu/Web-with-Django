import xlwings as xw
import MySQLdb
db = MySQLdb.connect(host="localhost", user="root", passwd="", db="EIA",charset = "utf8")
def getdata(db,ID):
    sql = 'SELECT * FROM eia_enterprise WHERE enterpriseId = ' + ID
    print(sql)
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
        db.commit()
    finally:
        db.close();
    return result;
def DicToList(dict,start,end):
    diclist = []
    i = 0
    for key in dict:
        if(i<start):
            i = i + 1
            continue
        if (i >= start & i < end):
            diclist.append(dict[i])
            i = i + 1
        if(i == end):
            break
    print(diclist)
    return diclist
def ExcToDataSheet(db,ID):
    app = xw.App(visible=False, add_book=False)
    app.display_alerts = False
    app.screen_updating = False
    # 文件位置：filepath，打开test文档，然后保存，关闭，结束程序
    filepath = r'D:\test.xlsm'
    wb = app.books.open(filepath)
    sht = wb.sheets['信息']
    result = getdata(db,ID)
    diclist = DicToList(result,1,18)
    sht.range('B1').options(transpose=True).value = diclist
    diclist = DicToList(result,18,36)
    sht.range('B19').options(transpose=True).value = diclist
    sht.range('B40').value = result[36]
    sht.range('B41').value = result[37]
    sht.range('B48').value = result[38]
    sht.range('B49').value = result[39]
    wb.save()
    wb.close()
    app.quit()
    return "success"
