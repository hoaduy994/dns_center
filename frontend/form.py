import re
from django import forms

class FormSearchBlacklist(forms.Form):
    domain = forms.CharField(required=False,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

class FormSearchWhitelist(forms.Form):
    domain = forms.CharField(required=False,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))