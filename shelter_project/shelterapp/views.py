from django.shortcuts import render, redirect
from .forms import AnimalForm, AdoptionForm, CustomUserCreationForm, AdopterForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Animal, ShelterLocation, Paycheck, MedicalRecord, Donation,AdoptionRequest, CustomUser, Adopter
from django.contrib import messages
from .forms import AnimalForm
from .forms import AdoptionForm
from .models import Paycheck, Staff

def submit_animal(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_animals')  # Redirect to the list page
    else:
        form = AnimalForm()

    return render(request, 'submit_animal.html', {'form': form})

def view_animals(request):
    animals = Animal.objects.all()
    medical_records = MedicalRecord.objects.all()
    return render(request, 'view_animals.html', {'animals': animals, 'medical_records': medical_records})

def view_shelters(request):
    shelters = ShelterLocation.objects.all()
    return render(request, 'view_shelters.html', {'shelters': shelters})

def view_paychecks(request):
    paychecks = Paycheck.objects.all()
    return render(request, 'view_paychecks.html', {'paychecks': paychecks})

def view_employees(request):
    employees = Staff.objects.all()
    return render(request, 'view_employees.html', {'employees': employees})

def view_donations(request):
    donations = Donation.objects.all()
    return render(request, 'view_donations.html', {'donations': donations})

def view_medical_records(request):
    medical_records = MedicalRecord.objects.all()
    animals = Animal.objects.all()
    return render(request, 'view_medical_records.html', {'medical_records': medical_records, 'animals': animals})

def medical_records_search(request):
    query = request.GET.get('q', '')  # Get the search term from the query parameter
    
    # If there's a search query, filter medical records based on it
    if query:
        medical_records = MedicalRecord.objects.filter(
            Q(diagnosis__icontains=query) |
            Q(animalID__name__icontains=query) |
            Q(staffID__firstName__icontains=query) |
            Q(staffID__lastName__icontains=query)
        )
    else:
        medical_records = MedicalRecord.objects.all()  # Show all records if no query is provided

    # Render the page with the medical records and the query
    return render(request, 'medical_records_search.html', {
        'medical_records': medical_records, 'query': query
    })

def default_page(request):
    return render(request, 'default_page.html')

def adoption_app(request):
    if request.method == 'POST':
        form = AdoptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adoption_app')
    else:
        form = AdoptionForm()
    
    return render(request, 'adoption_app.html', {'form': form})

def user_signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'user_signup.html', {'form': form})

@login_required
def after_login(request):
    if request.user.is_staff_user:
        return redirect('staff_dashboard')  # Replace with your staff dashboard URL
    else:
        return redirect('user_dashboard')  # Replace with your user dashboard URL

def add_adopters(request):
    if request.method == 'POST':
        form = AdopterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('default_page')
    else:
        form = AdopterForm()

    return render(request, 'add_adopters.html', {'form': form})