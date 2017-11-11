from django.conf.urls import url
from . import views
from . import form_getting

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='index'),
    url(r'^register/$', views.register, name='index'),
    url(r'^table/$', views.table, name='index'),
    url(r'^form-post/$', form_getting.form_post),
]