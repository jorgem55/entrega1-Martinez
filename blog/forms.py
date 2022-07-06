from django import forms

class FormMember(forms.Form):
    name = forms.CharField(max_length=20)
    bike = forms.CharField(max_length=20)
    buy_date = forms.DateField(required=True)
    
class SearchMember(forms.Form):
    name = forms.CharField(max_length=20, required=False)