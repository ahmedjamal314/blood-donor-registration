from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    phone = forms.CharField()
    address = forms.CharField(widget=forms.Textarea)
    blood_group = forms.ChoiceField(
        choices=[
            ("A+", "A+"), ("A-", "A-"), 
            ("B+", "B+"), ("B-", "B-"),
            ("O+", "O+"), ("O-", "O-"),
            ("AB+", "AB+"), ("AB-", "AB-")
        ]
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
