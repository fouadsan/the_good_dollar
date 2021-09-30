from django import forms
from django.forms import widgets
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Field, Submit

from .models import Profile, AddressBook


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email',
                  'phone', 'address', 'city', )


# AddressBook Add Form
class AddressBookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.add_input(
            Submit('submit', 'Submit', css_class='btn-primary'))
        self.helper.form_method = 'POST'
        super(AddressBookForm, self).__init__(*args, **kwargs)
        

    address = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control w100'}))
    
    mobile = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-3'}
    ))

 

    class Meta:
        model = AddressBook
        fields = ('address', 'mobile', 'status', )