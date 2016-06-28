from django.conf.urls import include, url
from django.contrib import admin

from .views import (
	epic_list,
	epic_create,
	epic_edit,
	epic_delete,
	epic_detail,
	)


urlpatterns = [
    
    url(r'^$',        epic_list),
    url(r'^create/$', epic_create),
    url(r'^list/$',   epic_list, name='list'),
    url(r'^delete/$', epic_delete),
    url(r'^detail/(?P<id>\d+)/$', epic_detail, name='detail'),
    url(r'^detail/(?P<id>\d+)/edit/$', epic_edit, name='edit'),
    url(r'^detail/(?P<id>\d+)/delete/$', epic_delete, name='delete'),
    
]
