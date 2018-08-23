from django import forms

from .models import ElihuPost

class PostForm(forms.ModelForm):

    class Meta:
        model = ElihuPost
        fields = ('title', 'text',)
