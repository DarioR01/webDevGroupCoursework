from django import forms
import datetime

class UserRegistration(forms.Form):
    name = forms.CharField(label="name", required=True)
    surname = forms.CharField(label="surname", required=True)
    email = forms.EmailField(label="email", required=True, widget=forms.EmailInput())
    password = forms.CharField(label="password", required=True, widget=forms.PasswordInput())
    date = forms.DateField(label="date of birthday", widget=forms.SelectDateWidget(years=range(1950, datetime.date.today().year)))


class UserLogin(forms.Form):
    email = forms.EmailField(label="email", required=True, widget=forms.EmailInput())
    password = forms.CharField(label="password", required=True, widget=forms.PasswordInput())