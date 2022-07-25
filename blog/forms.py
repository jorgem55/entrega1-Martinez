from unittest.util import _MAX_LENGTH
from django import forms

class FormMember(forms.Form):
    name = forms.CharField(max_length=20)
    bike = forms.CharField(max_length=20)
    buy_date = forms.DateField(required=True)
    
class SearchMember(forms.Form):
    name = forms.CharField(max_length=20, required=False)

class FormPost(forms.Form):
    title = forms.CharField(max_length=20)
    content=forms.Textarea()
    author = forms.CharField(max_length=20)
    creation_date = forms.DateField(required=True)
    
class SearchPost(forms.Form):
    title = forms.CharField(max_length=20, required=False)