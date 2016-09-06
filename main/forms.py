from django import forms
from . import models


class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        exclude = ["answer_text", "created_date", "confirmed"]
        widgets = {'user_text': forms.Textarea(attrs={'style': 'resize:none;'}),}


class EmailForm(forms.ModelForm):
    class Meta:
        model = models.Email
        exclude = ["created_date", "to_main"]
        widgets = {'user_text': forms.Textarea(attrs={'style': 'resize:none;'})}

