from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    
    url(r'^$', "epics.views.epic_list"),
    url(r'^create/$', "epics.views.epic_create"),
    url(r'^list/$', "epics.views.epic_list"),
    url(r'^edit/$', "epics.views.epic_edit"),
    url(r'^delete/$', "epics.views.epic_delete"),
    
]
