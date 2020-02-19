from django import forms
from .models import Post, Comment

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
