from django import forms
from .models import Subscription, Contact, Comments, Blog


class SubForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['email', ]


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['full_name', 'email', 'phone', 'message']
        exclude = ['blog',]
