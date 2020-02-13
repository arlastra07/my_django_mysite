from django import forms
from .models import Post

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
