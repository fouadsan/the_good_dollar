
from django import forms


class ContactMe(forms.Form):
    class Meta:
        name = forms.CharField(max_length=50)
        email = forms.EmailField()
        subject = forms.CharField(max_length=200)
        message = forms.CharField(widget=forms.Textarea)
