from django.db import models
from django.contrib.auth.models import AbstractUser


# from django.contrib.auth.models import User



class Enterprise(models.Model):
    enterpriseId = models.IntegerField(primary_key=True)  # 公司id primary_key
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
    environmentalProtectionInvestmentProtection = models.FloatField(null=True)  # 环保投资占比 default null
    floorSpace = models.IntegerField(null=True)  # 占地面积（m2) default null
    managementSpace = models.IntegerField(null=True)  # 经营面积(m2) default null
    nonAccommodationNum = models.IntegerField(null=True)  # 职工非住宿人数 default null
    accommodationNum = models.IntegerField(null=True)  # 职工住宿人数 default null
    stuffNum = models.IntegerField(null=True)  # 职工总人数 default null
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
    east = models.FloatField(null=True)  # 东 default null
    south = models.FloatField(null=True)  # 南 default null
    west = models.FloatField(null=True)  # 西 default null
    north = models.FloatField(null=True)  # 北 default null
    township = models.CharField(max_length=50, null=True)  # 所在区镇 default null

    def __str__(self):
        return self.enterpriseName


class Products(models.Model):
    productsId = models.IntegerField(primary_key=True)  # 产品id primary_key
    enterpriseId = models.ForeignKey(Enterprise, on_delete=models.CASCADE)  # 公司id foreign_key 多对一
    productsName = models.CharField(max_length=50, null=True)  # 产品名称 default null
    num = models.BigIntegerField(null=True)  # 数量 default null
    unit = models.CharField(max_length=20, null=True)  # 单位 not null

    def __str__(self):
        return self.productsName


class User(AbstractUser):
    enterpriseId = models.ForeignKey(Enterprise, on_delete=models.CASCADE)  # 公司id foreign_key 多对一
    REQUIRED_FIELDS = ['email', 'enterpriseId']
    # others inherited from AbstractUser
