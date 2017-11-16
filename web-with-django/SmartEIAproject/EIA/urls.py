from django.conf.urls import url
from . import form_getting
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^gis/$', views.gis, name='gis'),
    url(r'^form-post/$', form_getting.form_post),
    url(r'^table/$', views.table, name='index'),
]