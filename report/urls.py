from django.conf.urls import url,include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin

from django.views.generic import TemplateView
from .views import (
	complaint_create,
	complaint_detail,
	complaint_list,
	complaint_update,
	fir_create,
	copstatus_create,
	casestatus_create,
	login,
	caseclose,
	
	)

urlpatterns = [
	url(r'^createcomplaint$',complaint_create),
	url(r'^(?P<id>\d+)/createfir$',fir_create),
	url(r'^(?P<id>\d+)/createcopstatus$',copstatus_create),
	url(r'^(?P<id>\d+)/createcasestatus$',casestatus_create),
	url(r'^(?P<id>\d+)/closecase$',caseclose),
	url(r'^$', complaint_list,name="list"),
	url(r'^(?P<id>\d+)/edit$', complaint_update,name="update"),
	url(r'^(?P<id>\d+)/$', complaint_detail,name="detail"),
	
   
	]
