from django import forms
from first_app.models import PracticeModel

class PracticeForm(forms.ModelForm):
    class Meta:
        model = PracticeModel
        fields = '__all__'