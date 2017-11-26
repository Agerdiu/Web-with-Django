from django.conf.urls import url
from . import form_getting
from . import products_dealing
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^gis/$', views.gis, name='gis'),
    url(r'^form-post/$', form_getting.form_post),
    url(r'^products_submit/$', products_dealing.products_submit),
    url(r'^table/$', views.table, name='table'),
    url(r'^products/$', views.products, name='products'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^enterprise/download/(?P<enterpriseId>[0-9]+)/$', views.download, name='download'),

]