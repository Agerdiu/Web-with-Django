from django.contrib import admin
from .models import Enterprise, Product,User,Equipment,Material


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email','last_login','date_joined','is_manager']

class EnterpriseAdmin(admin.ModelAdmin):
    list_display = ['enterpriseName','createTime','updateTime']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['productsName']

class MaterialAdmin(admin.ModelAdmin):
    list_display = ['materialName']


class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['equipName']

admin.site.register(User,UserAdmin)
admin.site.register(Enterprise,EnterpriseAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Equipment,EquipmentAdmin)
admin.site.register(Material,MaterialAdmin)


# Register your models here.
