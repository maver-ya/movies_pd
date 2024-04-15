from django import forms

from .models import *


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['movie', 'comments', 'user']
        widgets = {
            "movie": forms.HiddenInput(),
            "user": forms.HiddenInput()
        }
