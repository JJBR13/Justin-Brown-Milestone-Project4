from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth.models import User

class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove labels for all fields
        for field_name, field in self.fields.items():
            field.label = ''

        # You can add custom placeholder text here if needed
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email address'
        self.fields['email2'].widget.attrs['placeholder'] = 'Confirm your email address'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter your username'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter your password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm your password'
        
        # Add any other customisation to the fields (like CSS classes)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ('username', 'email', 'email2', 'password1', 'password2')
