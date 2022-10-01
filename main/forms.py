from django.contrib.auth.forms import UserCreationForm
from django.forms import *
from django.contrib.auth.models import *

from main.models import DataUser


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        widgets = dict(
            username=TextInput(
                attrs=dict(
                    type='text'
                )
            ),
            password1=TextInput(
                attrs=dict(
                    type='password'
                )
            ),
            password2=TextInput(
                attrs=dict(
                    type='password'
                )
            ),
        )

class AddDataUser(ModelForm):
    class Meta:
        model = DataUser
        fields = ('Age', 'Logo', 'Status')