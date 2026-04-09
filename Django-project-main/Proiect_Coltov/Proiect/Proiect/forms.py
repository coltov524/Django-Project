from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in self.fields:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].label =""  
        self.fields['username'].widget.attrs.update({
            'placeholder': 'username',
            'class': 'input-field'
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'email',
            'class': 'input-field'
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'confirm password',
            'class': 'input-field'
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'password',
            'class': 'input-field'
        })