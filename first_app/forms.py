from django import forms
from django.core import validators 
from first_app.models import PracticeModel

class PracticeForm(forms.ModelForm):
    class Meta:
        model = PracticeModel
        fields = '__all__'



class ApiForm(forms.Form):
    name = forms.CharField(label="user Name")
    email = forms.EmailField(label="user Name")
    agree = forms.BooleanField()
    comment = forms.CharField(widget=forms.Textarea)
    value = forms.DecimalField()
    CHOICES =[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    size = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    




