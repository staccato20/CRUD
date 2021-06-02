from django import forms
from django.db import models
from django.forms import fields
from .models import Blog, Comment
class CreateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'writer', 'content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']