from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Animal, AdoptionRequest, CustomUser, Adopter, Staff, MedicalRecord, ShelterLocation, Donation
from django.utils.timezone import now  # For setting default donation date

class AnimalForm(forms.ModelForm):
    locationID = forms.ChoiceField(
        label='Location of Resident Shelter', 
        required=True,
        widget=forms.Select
    )

    adoptedOrNot = forms.ChoiceField(
        label='Adoption Status',
        choices=[(0, 'No'), (1, 'Yes')],
        widget=forms.Select,
        required=True
    )

    species = forms.ChoiceField(
        label='Species',
        choices=[('Dog', 'Dog'), ('Cat', 'Cat')],
        widget=forms.Select,
        required=True
    )

    gender = forms.ChoiceField(
        label='Gender',
        choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
        widget=forms.Select,
        required=True
    )
    
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
            'description': 'Description',
            'locationID': 'Location of Resident Shelter',
            'reasonForIntake': 'Reason for Intake',
            'adoptionFee': 'Adoption Fee'
        }

    def __init__(self, *args, **kwargs):
        super(AnimalForm, self).__init__(*args, **kwargs)
        
        # Populating the locationID choices with locationName and locationID
        locations = ShelterLocation.objects.all()
        location_choices = [
            (location.locationID, f"{location.locationName} ({location.locationID})" 
             if ShelterLocation.objects.filter(locationName=location.locationName).count() > 1 
             else location.locationName)
            for location in locations
        ]
        self.fields['locationID'].choices = location_choices
        
class AdoptionForm(forms.ModelForm):
    staffAdministrator = forms.ModelChoiceField(
        queryset=Staff.objects.all(),  # Fetch all staff members from the database
        empty_label="Select a Staff Member",  # Placeholder for the dropdown
        label="Staff Administrator"  # Label displayed in the form
    )
    
    class Meta:
        model = AdoptionRequest
        fields = ['dateAdopted', 'adoptionStatus', 'staffAdministrator']
        labels = {
            'dateAdopted': 'Date',
            'adoptionStatus': 'Application Status'
        }
        widgets = {
            'dateAdopted': forms.DateInput(attrs={'type': 'date'}),  # Add a date picker
        }


class EditAdoptionRequestForm(forms.ModelForm):
    dateAdopted = forms.CharField(required=False, max_length=10, initial='')  # Allow N/A to be entered as text
    
    class Meta:
        model = AdoptionRequest
        fields = ['adopterID', 'animalID', 'dateAdopted', 'adoptionStatus', 'staffAdministrator']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Disable fields that shouldn't be changed
        self.fields['adopterID'].disabled = True
        self.fields['animalID'].disabled = True
        self.fields['staffAdministrator'].disabled = True
        # Make dateAdopted optional
        self.fields['dateAdopted'].required = False
        # Set the default value for adoptionStatus to 'not_viewed'
        self.fields['adoptionStatus'].initial = 'not_viewed'
    
    def clean_dateAdopted(self):
        adoption_status = self.cleaned_data.get('adoptionStatus')
        date_adopted = self.cleaned_data.get('dateAdopted')
        
        if date_adopted == 'N/A':
            return None  # Set to None if 'N/A' is selected
        
        if adoption_status == 'accepted' and not date_adopted:
            raise forms.ValidationError("Adoption Date is required when status is 'Accepted'.")
        
        # Convert to proper date format if a date is entered
        try:
            if date_adopted:
                return forms.DateField().to_python(date_adopted)  # Convert the string to a Date
        except ValueError:
            raise forms.ValidationError("Invalid date format. Please enter a valid date.")
        
        return date_adopted

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

    # Inherit the password fields from UserCreationForm
    password1 = forms.CharField(widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = CustomUser  # Ensure you're using the CustomUser model
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'address', 'password1', 'password2')

    def save(self, commit=True):
        # Save the user
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password1'])  # Set the password securely

        if commit:
            user.save()

        # Create the adopter profile
        Adopter.objects.create(
            user=user,
            phone_number=self.cleaned_data['phone_number'],
            address=self.cleaned_data['address']
        )
        return user

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'phone_number', 'address']

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
        
class StaffAdminForm(forms.ModelForm):
    # Fields for CustomUser
    username = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=False)  # Optional password field

    # Field for phone number with (XXX) XXX-XXXX format validation
    phone_number = forms.RegexField(
        regex=r'^\(\d{3}\) \d{3}-\d{4}$',
        max_length=14,
        required=True,
        label="Phone Number",
        error_messages={
            'invalid': 'Phone number must be in the format (XXX) XXX-XXXX.'
        }
    )

    class Meta:
        model = Staff
        fields = ['position', 'phone_number', 'hireDate', 'salary']

    def save(self, commit=True):
        # First, create or retrieve the CustomUser
        username = self.cleaned_data['username']
        email = self.cleaned_data['email']
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        password = self.cleaned_data['password']

        if not self.instance.user_id:  # Check if this staff instance has an associated user
            # Create a new CustomUser if it doesn't exist
            user = CustomUser.objects.create_user(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                is_staff=True,
                password=password or 'defaultpassword123'  # Provide a default password if not set
            )
            # Now link this user to the Staff instance
            self.instance.user = user

        # Now create or update the Staff profile
        staff = super().save(commit=False)
        if commit:
            staff.save()  # Save the Staff profile

        return staff

class EditMedicalRecordForm(forms.ModelForm):
    animalID = forms.ModelChoiceField(queryset=Animal.objects.all(), required=False)
    staffID = forms.ModelChoiceField(queryset=Staff.objects.all(), required=False)
    diagnosis = forms.CharField(max_length=200, required=False)

    class Meta:
        model = MedicalRecord
        fields = ['animalID', 'staffID', 'diagnosis', 'treatment', 'date', 'note']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Disable fields that shouldn't be changed
        self.fields['animalID'].disabled = True
        self.fields['staffID'].disabled = True

    def save(self, commit=True):
        # Save the medical record first
        instance = super().save(commit=False)
        
        # Check if a diagnosis was provided and update the healthStatus accordingly
        if 'diagnosis' in self.cleaned_data and self.cleaned_data['diagnosis']:
            diagnosis = self.cleaned_data['diagnosis']
            
            # Update the health status of the associated animal to the diagnosis text
            instance.animalID.healthStatus = diagnosis
            instance.animalID.save()  # Save the updated animal record
        
        if commit:
            instance.save()
        return instance
    


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['locationID', 'amount', 'name', 'phone_number', 'email', 'address']
        widgets = {
            'phone_number': forms.TextInput(attrs={'placeholder': '(XXX) XXX-XXXX'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add placeholder and styling
        self.fields['name'].widget.attrs.update({'placeholder': 'Your Name'})
        self.fields['amount'].widget.attrs.update({'placeholder': 'Donation Amount'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Your Email'})
        self.fields['address'].widget.attrs.update({'placeholder': 'Your Address'})

        # You might want to ensure that 'locationID' is a dropdown (select box)
        self.fields['locationID'].queryset = ShelterLocation.objects.all()

    def save(self, commit=True):
        # Automatically set the donation date to today
        instance = super().save(commit=False)
        instance.donationDate = now().date()
        if commit:
            instance.save()
        return instance
