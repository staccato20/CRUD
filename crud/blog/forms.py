from django import forms
from .models import Blog
class CreateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'writer', 'content']