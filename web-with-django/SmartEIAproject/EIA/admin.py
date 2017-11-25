from django.contrib import admin
from .models import Enterprise, Product,User


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email','last_login','date_joined','is_manager']

class EnterpriseAdmin(admin.ModelAdmin):
    list_display = ['enterpriseName','createTime','updateTime']

admin.site.register(User,UserAdmin)
admin.site.register(Enterprise,EnterpriseAdmin)
admin.site.register(Product)


# Register your models here.
