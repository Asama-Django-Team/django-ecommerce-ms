from typing import Any
from django import forms
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("email", "phone_number", "full_name")

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password1"] and cd["password2"] and cd["password1"] != cd["password2"]:
            raise forms.ValidationError("passwords do not match")
        return cd["password2"]
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text="you can change password using <a href=\"../password\">this link</a>.")

    class Meta:
        model = User
        fields = ("email", "phone_number", "full_name", "password", "last_login")

class UserRegistrationForm(forms.Form):
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=11)
    full_name = forms.CharField(max_length=50)
    password = forms.CharField(label="password", widget=forms.PasswordInput())

    def clean_email(self):
        email = self.cleaned_data["email"]
        user = User.objects.filter(email=email).exists()
        if user:
            raise forms.ValidationError("email already exist")
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data["phone_number"]
        user = User.objects.filter(phone_number=phone_number).exists()
        if user:
            raise forms.ValidationError("phone_number already exist")
        return phone_number


    

    
