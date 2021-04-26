from django import forms
from django.contrib.auth import get_user_model
from .models import DevelopmentTasks

class DevelopmentForm(forms.ModelForm):
    class Meta:
        model = DevelopmentTasks
        fields = ('title', 'description', 'task_image' )


class SudoDevelopmentForm(forms.ModelForm):
    class Meta:
        model = DevelopmentTasks
        fields = ('response', 'status', )
