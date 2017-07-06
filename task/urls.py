from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^task_list/$', views.task_list, name='task_list'),

    #url(r'^task/complete$', views.task_complete, name='task_complete').
    #url(r'^task/new/$', views.task_new, name='task_new'),
    #url(r'^task/(?P<pk>[0-9]+)/edit/$', views.task_edit, name='task_edit'),
    url(r'^task/(?P<pk>[0-9]+)/$', views.task_detail, name='task_detail'),
    url(r'^task_complete_list/$', views.task_complete_list, name='task_complete_list'),
    url(r'^register/$', views.RegistrationView, name='register'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),


]
