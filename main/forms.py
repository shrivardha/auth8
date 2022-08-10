from django import forms
class CreateNewInfo(forms.Form):
    topic=forms.CharField(label="Topic",max_length=200)
    name=forms.CharField(label="Name",max_length=200)
    
