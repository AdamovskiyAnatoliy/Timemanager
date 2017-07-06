from django.conf.urls import url
from . import views

urlpatterns = [
<<<<<<< HEAD
    url(r'^$', views.task_list, name='task_list'),

=======
    url(r'^$', views.main, name='main'),
    url(r'^task_list/$', views.task_list, name='task_list'),
>>>>>>> bedf95df6b0b4272b0871764a837c8c76dcafaea
    #url(r'^task/complete$', views.task_complete, name='task_complete').
    url(r'^task/(?P<pk>[0-9]+)/$', views.task_detail, name='task_detail'),
    url(r'^task_complete_list/$', views.task_complete_list,name='task_complete_list'),
    url(r'^task/(?P<pk>[0-9]+)/edit/$', views.task_edit, name='task_edit'),
<<<<<<< HEAD
    #url(r'^task/new/$', views.task_new, name='task_new'),
    #url(r'^task/(?P<pk>[0-9]+)/edit/$', views.task_edit, name='task_edit'),
=======
>>>>>>> bedf95df6b0b4272b0871764a837c8c76dcafaea
]
