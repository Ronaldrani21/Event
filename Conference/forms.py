from django import forms
from Conference.models import Registrationform

CHOICES = [
    ("Mbarara","Mbarara"),
    ("Kabale","Kabale")
]

Programs = [
    ("BSCS","BSCS"),
    ("LAW","LAW")

]
class RegistrationForm(forms.ModelForm):
    Firstname           = forms.CharField(widget=forms.TextInput(attrs={ "type":"text", "class":"form-control", "placeholder":"First Name", "id":"fname",  }))
    Lastname            = forms.CharField(widget=forms.TextInput(attrs={"type":"text", "class":"form-control",  "placeholder":"Last Name", "id":"lname",  }))
    Email               = forms.CharField(widget=forms.TextInput(attrs={ "type":"email", "class":"form-control",  "placeholder":"Email", "id":"email",  }))
    Phone               = forms.CharField(widget=forms.TextInput(attrs={  "type":"text", "class":"form-control",  "placeholder": "Phone", "id":"cell" ,}))
    Address            = forms.CharField(widget=forms.TextInput(attrs={  "type":"text", "class":"form-control", "placeholder":"Address", "id":"address" }))
    City               = forms.CharField( widget=forms.Select(choices=CHOICES,attrs={ "class":"form-control", "name":"city" ,"id":"city" }))  #
    program               = forms.CharField(widget=forms.Select(choices=Programs,attrs={ "class":"form-control", "name":"program", "id":"program"})) 
    class Meta:
        model = Registrationform
        fields="__all__"



