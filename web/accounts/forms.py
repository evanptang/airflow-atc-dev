from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

# from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        label='First Name',
        error_messages={'exists': 'Oops'}
    )
    last_name = forms.CharField(
        required=True,
        label='Last Name',
        error_messages={'exists': 'Oops'}
    )
    email = forms.EmailField(
        required=True,
        label='Email',
        error_messages={'exists': 'Oops'}
    )
    class Meta(UserCreationForm):
        model = get_user_model()
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2') # new



class SignupForm(forms.Form):
    first_name = forms.CharField(
        required=True,
        label='First Name',
        max_length=35,
    )
    last_name = forms.CharField(
        required=True,
        label='Last Name',
        max_length=35,
    )

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
