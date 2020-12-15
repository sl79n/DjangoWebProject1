"""
Definition of forms.
"""

from django import forms
from django.db import models
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from .models import Comment, Blog

class AnketaForm(forms.Form):
    name = forms.CharField(label='Ваше имя', min_length=2, max_length=100)
    city = forms.CharField(label='Ваш город', min_length=2, max_length=100)
    email = forms.EmailField(label='Ваш e-mail', min_length=7)
    message = forms.CharField(label='Опишите вашу проблему',
                              widget=forms.Textarea(attrs={'rows':12, 'cols':20}))

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class CommentForm(forms.ModelForm):
   class Meta:
       model = Comment
       fields = ('text',)
       labels = {'text': ""}

class BlogForm(forms.ModelForm):
   class Meta:
       model = Blog
       fields = ('title','description','content', 'posted', 'image')
       labels = {'title': "Заголовок", 'image': "", 'description': "Краткое описание", 'content': "Содержание", 'posted': "Дата",}