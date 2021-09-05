from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, SetPasswordForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Submit

from .models import Profile, AddressBook
    
class UserRegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_show_labels = False

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Username', 'id': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Email', 'id': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control mb-3',
            'placeholder': 'Password1',
            'id': 'Password1',
        }

    ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control mb-3',
            'placeholder': 'Password2',
            'id': 'Password2',
        }

    ))


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email',
                  'phone', 'address', 'city', )



class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_show_labels = False

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Username', 'id': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control mb-3',
            'placeholder': 'Password',
            'id': 'Password'
        }

    ))


class ResetPasswordForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(ResetPasswordForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_show_labels = False

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Email', 'id': 'Email'}))


class ResetPasswordConfirmForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(ResetPasswordConfirmForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_show_labels = False

    new_password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control mb-3',
            'placeholder': 'New Password',
            'id': 'Password1'
        }

    ))
    new_password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control mb-3',
            'placeholder': 'Confim Password',
            'id': 'Password2'
        }

    ))


# AddressBook Add Form
class AddressBookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('name', id="id_updateName"),
            Field('mobile', id="id_updateMobile"),
            Field('status', id="id_updateStatus"),
        )
        self.helper.add_input(
            Submit('submit', 'Submit', css_class='btn-primary'))
        self.helper.form_method = 'POST'
        super(AddressBook, self).__init__(*args, **kwargs)

    class Meta:
        model = AddressBook
        fields=('address','mobile','status')