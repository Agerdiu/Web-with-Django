from django import forms
from .models import Enterprise, User,Product,Equipments,Materials


class EnterpriseForm(forms.ModelForm):
    class Meta:
        model = Enterprise
        fields = ['enterpriseName','nameAbbreviation','NEIType','environmentAssessmentCompany','corporateName','corporateId','contacts','telephone','postalCode',
                  'address','totalInvestment','environmentalProtectionInvestment','environmentalProtectionInvestmentProportion',
                  'floorSpace','managementSpace','nonAccommodationNum','accommodationNum','dayWorkTime','yearWorkTime',
                  'investmentTime','productNames','constructionScale','noiseEquipment','noiseMonitoringPoints',
                  'annualSolidWasteOutput','annualPowerConsumption','latitude','longtitude','east','south','west',
                  'north','township','soundEnvironmentStandard','groundwaterArea','specialOptionforDaliang',
                  'besideWaterTreatmentPlant','sensitivePointDistance','waterSourceDistance']


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'telephone', 'email', 'password', 'is_manager','environmentAssessmentCompany']



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['productsName','num','unit','remark']


class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipments
        fields = ['equipName','num','unit','remark']



class MaterialForm(forms.ModelForm):
    class Meta:
        model = Materials
        fields = ['materialName','num','unit','isOffcut','state']
