from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^$', views.task_list, name='task_list'),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),


    #url(r'^task/complete$', views.task_complete, name='task_complete').
    url(r'^(?P<pk>[0-9]+)/$', views.task_detail, name='task_detail'),
    url(r'^new/$', views.task_new, name='task_new'),
    url(r'^task_complete_list/$', views.task_complete_list,name='task_complete_list'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.task_edit, name='task_edit'),
    #url(r'^task/new/$', views.task_new, name='task_new'),
    #url(r'^task/(?P<pk>[0-9]+)/edit/$', views.task_edit, name='task_edit'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),

]
