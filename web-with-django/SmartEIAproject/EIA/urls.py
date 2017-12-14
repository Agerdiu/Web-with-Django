from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^manage/$', views.manage, name='manage'),
    url(r'^workerManage/$', views.workerManage, name='workerManage'),
    url(r'^managerManage/$', views.managerManage, name='managerManage'),
    url(r'^agencyManage/$', views.agencyManage, name='agencyManage'),
    url(r'^products/(?P<enterpriseId>[0-9]+)/$', views.products, name='products'),
    url(r'^materials/(?P<enterpriseId>[0-9]+)/$', views.materials, name='materials'),
    url(r'^equipments/(?P<enterpriseId>[0-9]+)/$', views.equipments, name='equipments'),
    url(r'^createGisForm/$', views.createGisForm, name='createGisForm'),
    url(r'^upload/(?P<enterpriseId>[0-9]+)/$', views.upload, name='upload'),
    url(r'^updateStateType/$', views.updateStateType, name='updateStateType'),
    url(r'^enterprise/download/(?P<enterpriseId>[0-9]+)/(?P<target>[a-zA-Z]+)/$', views.download, name='download'),
    url(r'^changeInfo/$', views.changeInfo, name='changeInfo')
]