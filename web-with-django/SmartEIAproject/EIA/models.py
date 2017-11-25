from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    manager = models.ForeignKey('self', null=True)
    is_manager = models.BooleanField(default=False)
    telephone = models.CharField(max_length=15, null=True)
    environmentAssessmentCompany = models.CharField(max_length=255, null=True)  # 环评公司名称 default null

'''
class Manager(models.Model):
    managerId = models.AutoField(primary_key=True)  # 经理id primary_key
    userId = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 用户id foreign_key 一对一
'''
'''
class Worker(models.Model):
    workerId = models.AutoField(primary_key=True)  # 员工id primary_key
    userId = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 用户id foreign_key 一对一
    managerId = models.ForeignKey(Manager, on_delete=models.CASCADE)  # 经理id foreign_key 多对一
'''

class Enterprise(models.Model):
    enterpriseId = models.AutoField(primary_key=True)  # 公司id primary_key
    workerId = models.ForeignKey('User', on_delete=models.CASCADE)  # 管理员工id foreign_key 多对一
    createTime=models.DateTimeField(auto_now_add=True)  # 创建时间
    durationTime=models.DateTimeField(null=True)  # 进行天数
    updateTime=models.DateTimeField(auto_now=True)  # 更新时间
    NEIType = models.CharField(max_length=255, null=True)  # 国民经济行业类别及代码 default null
    nameAbbreviation = models.CharField(max_length=255, null=True)  # 名称缩写 default null
    enterpriseName = models.CharField(max_length=255, null=True)  # 公司名称 default null
    environmentAssessmentCompany = models.CharField(max_length=255, null=True)  # 环评公司名称 default null
    corporateId = models.CharField(max_length=18,null=True)  # 法人身份证 default null
    corporateName = models.CharField(max_length=10, null=True)  # 法人代表姓名 default null
    contacts = models.CharField(max_length=10, null=True)  # 联系人 default null
    telephone = models.CharField(max_length=20, null=True)  # 联系电话 default null
    postalCode = models.CharField(max_length=6, null=True)  # 邮政编码 default null
    address = models.CharField(max_length=20, null=True)  # 地址 default null
    totalInvestment = models.IntegerField(null=True)  # 项目总投资（万元） default null
    environmentalProtectionInvestment = models.IntegerField(null=True)  # 环保投资（万元） default null
    environmentalProtectionInvestmentProportion = models.FloatField(null=True)  # 环保投资占比 default null
    floorSpace = models.IntegerField(null=True)  # 占地面积（m2) default null
    managementSpace = models.IntegerField(null=True)  # 经营面积(m2) default null
    nonAccommodationNum = models.IntegerField(null=True)  # 职工非住宿人数 default null
    accommodationNum = models.IntegerField(null=True)  # 职工住宿人数 default null
    dayWorkTime = models.IntegerField(null=True)  # 日工作时间 default null
    yearWorkTime = models.IntegerField(null=True)  # 年工作时间 default null
    investmentTime = models.IntegerField(null=True)  # 投资时间(年) default null
    productNames = models.CharField(max_length=255, null=True)  # 产品名称 顿号相隔 default null
    constructionScale = models.CharField(max_length=50, null=True)  # 建设规模 default null
    noiseEquipment = models.CharField(max_length=50, null=True)  # 噪声污染源设备 default null
    noiseMonitoringPoints = models.IntegerField(null=True)  # 噪声监测点数目 default null
    annualSolidWasteOutput = models.FloatField(null=True)  # 包装袋年产量(t/a) default null
    annualPowerConsumption = models.FloatField(null=True)  # 电年耗量(万kwh/a) default null
    latitude = models.FloatField(null=True)  # 纬度 default null
    longtitude = models.FloatField(null=True)  # 经度 default null
    east = models.CharField(max_length=50, null=True)  # 东 default null
    south = models.CharField(max_length=50, null=True)  # 南 default null
    west = models.CharField(max_length=50, null=True)  # 西 default null
    north = models.CharField(max_length=50, null=True)  # 北 default null
    township = models.CharField(max_length=50, null=True)  # 所在区镇 default null
    soundEnvironmentStandard = models.CharField(max_length=5, null=True) # 声环境质量标准 default null
    groundwaterArea = models.CharField(max_length=50, null=True)  # 地下水区域 default null
    specialOptionforDaliang = models.CharField(max_length=5, null=True)  # 大良特别选项 default null
    besideWaterTreatmentPlant = models.CharField(max_length=5, null=True)  # 是否污水处理厂纳污范围 default null
    sensitivePointDistance = models.CharField(max_length=5, null=True) # 敏感点距离 default null
    waterSourceDistance = models.CharField(max_length=5, null=True) # 水源保护地距离 default null
    def __str__(self):
        return self.enterpriseName


    def get_upload_url(self):
        return reverse('upload', kwargs={'enterpriseId': self.enterpriseId})

    def get_download_url(self):
        return reverse('download', kwargs={'enterpriseId': self.enterpriseId})


class Product(models.Model):
    productsId = models.AutoField(primary_key=True)  # 产品id primary_key
    enterpriseId = models.ForeignKey(Enterprise, on_delete=models.CASCADE)  # 公司id foreign_key 多对一
    productsName = models.CharField(max_length=50, null=True)  # 产品名称 default null
    num = models.BigIntegerField(null=True)  # 数量 default null
    unit = models.CharField(max_length=20, null=True)  # 单位 not null
    remark = models.CharField(max_length=50, null=True)  # 备注 default null
    def __str__(self):
        return self.productsName



class Materials(models.Model):
    materialId = models.AutoField(primary_key=True)  # Field name made lowercase.
    materialName = models.CharField(max_length=50)  #Field name made lowercase.
    num = models.FloatField(null=True)
    unit = models.CharField(max_length=20, null=True)
    isOffcut = models.CharField(max_length=5,null=True)  # Field name made lowercase.
    state = models.CharField(max_length=10,null=True)
    enterpriseId = models.ForeignKey(Enterprise, on_delete=models.CASCADE)  # Field name made lowercase.
    def __str__(self):
        return self.materialName



class Equipments(models.Model):
    equipId = models.AutoField(primary_key=True)  # Field name made lowercase.
    equipName = models.CharField( max_length=50)  # Fieldname made lowercase.
    num = models.IntegerField(null=True)
    unit = models.CharField(max_length=50, null=True)
    remark = models.CharField(max_length=255,null=True)
    enterpriseId = models.ForeignKey(Enterprise, on_delete=models.CASCADE)  # Field name made lowercase.
    def __str__(self):
        return self.equipName
