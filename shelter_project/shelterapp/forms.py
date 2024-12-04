from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Animal, AdoptionRequest, CustomUser, Adopter, Staff, MedicalRecord

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['name', 'species', 'breed', 'age', 'gender', 'dateOfArrival', 
                  'adoptedOrNot', 'healthStatus', 'description', 'locationID', 
                  'reasonForIntake', 'adoptionFee']
        labels = {
            'name': 'Name',
            'species': 'Species',
            'breed': 'Breed',
            'age': 'Age',
            'gender': 'Gender',
            'dateOfArrival': 'Date of Arrival',
            'adoptedOrNot': 'Adoption Status',
            'healthStatus': 'Health Status',
            'discription': 'Discription',
            'locationID': 'Location of Resident Shelter',
            'reasonForIntake': 'Reason for Intake',
            'adoptionFee': 'Adoption Fee'
        }
        
class AdoptionForm(forms.ModelForm):
    class Meta:
        model = AdoptionRequest
        fields = ['dateAdopted', 'adoptionStatus']
        widgets = {
            'dateAdopted': forms.DateInput(attrs={'type': 'date'}),  # Add a date picker
        }

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser  # Dynamically fetch the custom user model
        fields = ['username', 'email', 'password1', 'password2']  # Adjust as needed
        
class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ['animalID', 'staffID', 'diagnosis', 'treatment', 'date', 'note']
        label = {
            'animalID': 'Animal ID',
            'staffID': 'Staff ID',
            'diagnosis': 'Diagnosis',
            'treatment': 'Treatment',
            'date': 'Date',
            'note': 'Note'
        }
        widgets = {
            'dateAdopted': forms.DateInput(attrs={'type': 'date'}),  # Add a date picker
        }