from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def epic_create(request=None):

	return HttpResponse("<h1> Creating Epic!! </h1>")


def epic_detail(request=None):

	return HttpResponse("<h1> Here is 1 Epic!! </h1>")


def epic_list(request=None):

	#return HttpResponse("<h1> The list of Epics!! </h1>")
	return render(request, "index.html",{})


def epic_edit(request=None):

	return HttpResponse("<h1> Change the Epic here!! </h1>")


def epic_delete(request=None):

	return HttpResponse("<h1> The epic is gone!! </h1>")