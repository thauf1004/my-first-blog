from django import forms

from .models import Post, Comment

class MenuForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('menu_id', 'text',)
