from django.contrib.auth import forms
from django.contrib.auth.models import User
from .models import UserInformation, CustomUser

class CustomUserCreationForm(forms.UserCreationForm):
    class Meta:
        model = CustomUser
        fields = forms.UserCreationForm.Meta.fields + ('age', 'address',)

class UserInformationForm(forms.UserCreationForm):
    class Meta:
        model = UserInformation
        fields = ['age', 'address']