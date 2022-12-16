from django import forms
import datetime

class UserRegistration(forms.Form):
    name = forms.CharField(label="name", required=True, widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control mb-3'}))
    surname = forms.CharField(label="surname", required=True, widget=forms.TextInput(attrs={'placeholder': 'Surname', 'class': 'form-control mb-3'}))
    email = forms.EmailField(label="email", required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control mb-3'}))
    password = forms.CharField(label="password", required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control mb-3'}))
    date = forms.DateField(label="date of birthday", required=True, widget=forms.SelectDateWidget(years=range(1950, datetime.date.today().year), attrs={'placeholder': 'Password', 'class': 'form-select m-1 mb-3'}))


class UserLogin(forms.Form):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control mb-3'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control mb-3'}))