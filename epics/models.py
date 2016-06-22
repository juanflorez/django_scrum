from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Epic(models.Model):
    title   =  models.CharField(max_length = 120)
    content =  models.TextField()
    points  =  models.IntegerField()


    def __str__(self):  
	    return self.title

    def __unicode__(self): 
	    return self.title


    def get_absolute_url(self):
    	return reverse("detail", kwargs={"id": self.id})
        