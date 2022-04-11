from email import message
from django import forms


class Contact(forms.Form):
    name = forms.CharField(max_length=40,  min_length=30, widget=forms.TextInput(attrs={'placeholder':'name'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'message', 'style':'resize:none;'}))
    password = forms.CharField(max_length=40,  min_length=30, widget=forms.TextInput(attrs={'placholder':'name'}))
