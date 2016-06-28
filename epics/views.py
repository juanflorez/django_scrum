from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .forms import EpicForm


# Create your views here.
from .models import Epic


def epic_create(request):
    form = EpicForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "The Epic was created")
        return HttpResponseRedirect(instance.get_absolute_url())
       
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


def epic_edit(request, id):

    instance = get_object_or_404(Epic, id=id)
    form     = EpicForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "The epic was edited")
        return HttpResponseRedirect(instance.get_absolute_url())    
    context  = {
         "title": instance.title,
         "instance": instance,
         "form": form,

    }
    
    return render(request, "Epic_edit.html", context)
    

def epic_detail(request, id):
    
    instance = get_object_or_404(Epic, id=id) 
    context = {
      "title": instance.title,
      "content": instance.content,
      "points": instance.points,

    }
    return render(request, "Epic_read_detail.html", context)


def epic_delete(request, id):
    instance = get_object_or_404(Epic, id=id)
    instance.delete()
    messages.success(request, "The Epic was deleted", extra_tags=str(id))
    return redirect("epics:list")
