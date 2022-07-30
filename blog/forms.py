from enum import unique
from pydoc import text
from tkinter import ALL
from tkinter.tix import Form
from django import forms
from ckeditor.fields import RichTextFormField
class FormMember(forms.Form):
    name = forms.CharField(max_length=20)
    bike = forms.CharField(max_length=20)
    buy_date = forms.DateField(required=True)
    class Meta:
        help_texts = None
    
class SearchMember(forms.Form):
    name = forms.CharField(max_length=20, required=False)

class FormPost(forms.Form):
    title = forms.CharField(max_length=20)
    # subtitle=forms.CharField(max_length=20)
    content = RichTextFormField()
    author = forms.CharField(max_length=20)
    creation_date = forms.DateField(required=False)
    # image = forms.ImageField(required=False)
    class Meta:
        help_texts = None
        
class SearchPost(forms.Form):
    title = forms.CharField(max_length=20, required=False)