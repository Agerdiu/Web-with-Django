from django.contrib import admin
from .models import Enterprise, Products, User

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'enterpriseId']


admin.site.register(Enterprise)
admin.site.register(Products)
admin.site.register(User, UserAdmin)


# Register your models here.
