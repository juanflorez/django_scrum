from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.
from .models import Epic


def epic_create(request=None):

	return HttpResponse("<h1> Creating Epic!! </h1>")


def epic_list(request=None):

    queryset = Epic.objects.all()
    context = {
	    "epics_list": queryset
	}
    return render(request, "Epics_list.html", context)


def epic_edit(request=None):

	return HttpResponse("<h1> Change the Epic here!! </h1>")

def epic_detail(request, id):
    
    instance = get_object_or_404(Epic, id=id) 
    context = {
      "title": instance.title,
      "content": instance.content,

    }
    return render(request, "Epic_read_detail.html", context)


def epic_delete(request=None):

	return HttpResponse("<h1> The epic is gone!! </h1>")