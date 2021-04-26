from django import forms
from .models import Action

class ActionForm(forms.ModelForm):
    class Meta:
        model = Action
        exclude = ["user_added", "active", "pending_confirmation"]