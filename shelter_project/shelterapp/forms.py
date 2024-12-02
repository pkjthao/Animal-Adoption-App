from django import forms
from .models import Animals
from .models import AdoptionRequests

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animals
        fields = ['name', 'species', 'breed', 'age', 'gender', 'dateOfArrival', 
                  'adoptedOrNot', 'healthStatus', 'description', 'locationID', 
                  'reasonForIntake', 'adoptionFee']
        
class AdoptionForm(forms.ModelForm):
    class Meta:
        model = AdoptionRequests
        fields = ['dateAdopted', 'adoptionStatus']
