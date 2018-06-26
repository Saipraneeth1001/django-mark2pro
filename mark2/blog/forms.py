from django import forms
from blog.models import Post, Comment
from django.contrib.auth import get_user_model
from accounts.models import User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post

        fields = ('user_name', 'title', 'text')

        widget = {

            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'content': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }
