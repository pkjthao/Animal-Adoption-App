from django import forms
from .models import Animals

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animals
        fields = ['name', 'species', 'breed', 'age', 'gender', 'dateOfArrival', 
                  'adoptedOrNot', 'healthStatus', 'description', 'locationID', 
                  'reasonForIntake', 'adoptionFee']
