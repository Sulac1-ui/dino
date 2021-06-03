from django import forms
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.core.checks.messages import Error
from django.db.models.expressions import Exists
from django.forms.models import ModelForm
from .models import Order, Customer


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["ordered_by", "shipping_address",
                  "mobile", "email", "payment_method"]


class registerForm(ModelForm):

    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.CharField(widget=forms.EmailInput())
    Phonenumber = forms.CharField(max_length=10)

    class Meta:
        model = Customer
        managed = True
        fields = ["full_name", "username", "address",
                  "email", "password", "Phonenumber"]

    def clean_username(self):
        uname = self.cleaned_data.get("username")
        if User.objects.filter(username=uname).exists():
            raise forms.ValidationError(
                'Customer with this username already exists please pick another one.')

        return uname


class loginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
