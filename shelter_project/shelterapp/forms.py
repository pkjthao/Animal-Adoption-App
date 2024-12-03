from django import forms
from .models import Animals, AdoptionRequests, Adopters

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
        
class AdopterForm(forms.ModelForm):
    class Meta:
        model = Adopters
        fields = ['adopterID', 'firstName', 'lastName', 'phoneNumber', 'email', 'address', 'password']
        
    def clean_adopterID(self):
        adopterID = self.cleaned_data.get('adopterID')
        if Adopters.objects.filter(adopterID=adopterID).exists():
            raise forms.ValidationError('An adopter with this ID already exists. Please use a different ID.')
        return adopterID