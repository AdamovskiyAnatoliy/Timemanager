from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

from . import views


urlpatterns = [
    url(r'^$', views.task_list, name='task_list'),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),

    url(r'^task_detail/(?P<pk>[0-9]+)$', views.task_detail, name='task_detail'),
    url(r'^task_detail_complete(?P<pk>[0-9]+)$', views.task_detail_complete, name='task_detail_complete'),
    url(r'^new/$', views.task_new, name='task_new'),
    url(r'^task_complete_list/$', views.task_complete_list,name='task_complete_list'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.task_edit, name='task_edit'),

    url(r'^dreams_list/$', views.dreams_list, name='dreams_list'),
    url(r'^dreams_new/$', views.dreams_new, name='dreams_new'),
    url(r'^dream_detail/(?P<pk>[0-9]+)$', views.dream_detail, name='dream_detail'),

    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
]
