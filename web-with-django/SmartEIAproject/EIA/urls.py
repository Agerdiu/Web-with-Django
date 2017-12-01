from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^gis/$', views.gis, name='gis'),
    url(r'^manage/$', views.manage, name='manage'),
    url(r'^products/(?P<enterpriseId>[0-9]+)/$', views.products, name='products'),
    url(r'^materials/(?P<enterpriseId>[0-9]+)/$', views.materials, name='materials'),
    url(r'^equipments/(?P<enterpriseId>[0-9]+)/$', views.equipments, name='equipments'),
    url(r'^createGisForm/$', views.createGisForm, name='createGisForm'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^enterprise/download/(?P<enterpriseId>[0-9]+)/$', views.download, name='download')
]