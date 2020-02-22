from django import forms
from .models import Post, Comment
# ADDING LIBRARIES FOR CRISPY forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import (PrependedText, PrependedAppendedText, FormActions )

from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(
        attrs={
            'class':'form-control',
            'placeholder': 'Write a post ...'
        }
    ))
    class Meta:
        model = Post
        fields = ('title', 'text')

class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(
        attrs={
            'class':'form-control',
            'placeholder': 'Write a comment ...'
        }
    ))
    class Meta:
        model = Comment
        fields = ('text',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('Sign up','Sign up', css_class='btn-primary'))
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)
