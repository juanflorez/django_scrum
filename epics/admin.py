from django.contrib import admin

# Register your models here.
from epics.models import Epic

class EpicModelAdmin(admin.ModelAdmin):
	list_display = ["__str__","title","points"]
	list_filter = ["points"]
	search_field =["title"]
	class Meta:
		model = Epic

admin.site.register(Epic, EpicModelAdmin)
