from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Animal, AdoptionRequest, CustomUser

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['name', 'species', 'breed', 'age', 'gender', 'dateOfArrival', 
                  'adoptedOrNot', 'healthStatus', 'description', 'locationID', 
                  'reasonForIntake', 'adoptionFee']
        
class AdoptionForm(forms.ModelForm):
    class Meta:
        model = AdoptionRequest
        fields = ['dateAdopted', 'adoptionStatus']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser  # Dynamically fetch the custom user model
        fields = ['username', 'email', 'password1', 'password2']  # Adjust as needed