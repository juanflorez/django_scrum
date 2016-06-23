from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import EpicForm


# Create your views here.
from .models import Epic


def epic_create(request):
    form = EpicForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

       
    context = {
        "form": form,
    }
    return render(request, "Epic_edit.html", context )


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
      "points": instance.points,

    }
    return render(request, "Epic_read_detail.html", context)


def epic_delete(request=None):

	return HttpResponse("<h1> The epic is gone!! </h1>")