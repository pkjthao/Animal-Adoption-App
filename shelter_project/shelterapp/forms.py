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

class CombinedAdopterSignupForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    phone_number = forms.RegexField(
        regex=r'^\(\d{3}\) \d{3}-\d{4}$',
        max_length=14,
        required=True,
        label="Phone Number",
        error_messages={
            'invalid': 'Phone number must be in the format (XXX) XXX-XXXX.'
        }
    )
    address = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 1}),
        required=True,
        label="Address"
    )
    email = forms.EmailField(required=True)

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser  # Dynamically fetch the custom user model
        fields = ['username', 'email', 'password1', 'password2']  # Adjust as needed
        
class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'phone_number', 'address']

# this is the testing password: 12cas321s
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