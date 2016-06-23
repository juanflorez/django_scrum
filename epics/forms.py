from django import forms 
from .models import Epic

class EpicForm(forms.ModelForm):
    class Meta:
        model = Epic
        fields = [
            "title",
            "content",
            "points",

        ]
    
