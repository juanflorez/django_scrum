from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Epic


def epic_create(request=None):

	return HttpResponse("<h1> Creating Epic!! </h1>")


def epic_detail(request=None):

	return HttpResponse("<h1> Here is 1 Epic!! </h1>")


def epic_list(request=None):

    queryset = Epic.objects.all()
    context = {
	    "object_list": queryset
	}
    return render(request, "index.html", context)


def epic_edit(request=None):

	return HttpResponse("<h1> Change the Epic here!! </h1>")


def epic_delete(request=None):

	return HttpResponse("<h1> The epic is gone!! </h1>")