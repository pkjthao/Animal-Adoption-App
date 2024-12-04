from django.shortcuts import render, redirect
from .forms import AnimalForm, AdoptionForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Animal, ShelterLocation, Paycheck, MedicalRecord, Donation, AdoptionRequest, CustomUser, Adopter
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import AnimalForm, AdoptionForm, CombinedAdopterSignupForm
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

def user_logout(request):
    logout(request)  # Logs out the user
    return redirect('adopter_login')  # Redirect to login page after logging out

def adopter_signup(request):
    if request.method == 'POST':
        form = CombinedAdopterSignupForm(request.POST)
        if form.is_valid():
            # Create the user with first_name and last_name
            user = CustomUser.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],  # Add first_name
                last_name=form.cleaned_data['last_name'],    # Add last_name
                is_staff_user=False  # Ensure this is an adopter
            )

            # Create the adopter profile
            Adopter.objects.create(
                user=user,
                phone_number=form.cleaned_data['phone_number'],
                address=form.cleaned_data['address']
            )

            # Log the user in after creating the user and profile
            login(request, user)

            # Redirect to the user dashboard after successful signup
            return redirect('adopter_dashboard')  # Replace with the actual URL name for the user dashboard
        else:
            # If the form is not valid, show the form again with errors
            return render(request, 'adopter_signup.html', {'form': form})
    else:
        form = CombinedAdopterSignupForm()

    return render(request, 'adopter_signup.html', {'form': form})

def adopter_login(request):
    # Check if the user is already logged in
    if request.user.is_authenticated:
        # Redirect to the appropriate dashboard based on user type (adopter or staff)
        if request.user.is_staff:
            return redirect('staff_dashboard')  # Replace with actual staff dashboard URL name
        else:
            return redirect('adopter_dashboard')  # Replace with actual adopter dashboard URL name

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Log the user in
            
            # Check if 'next' is provided in the request and redirect to that URL, otherwise to the dashboard
            next_url = request.POST.get('next')  # Get next from POST (this is passed in the login form)
            if not next_url:
                # Redirect to adopter or staff dashboard based on the user type
                if user.is_staff:
                    next_url = reverse('staff_dashboard')  # Replace with actual staff dashboard URL
                else:
                    next_url = reverse('adopter_dashboard')  # Replace with actual adopter dashboard URL
            return HttpResponseRedirect(next_url)  # Redirect to the correct page
        else:
            # Invalid login, show error message
            return render(request, 'adopter_login.html', {'error': 'Invalid login credentials'})

    return render(request, 'adopter_login.html')

def staff_login(request):
    # Check if the user is already logged in
    if request.user.is_authenticated:
        # Redirect to the staff dashboard if the user is staff
        if request.user.is_staff:
            return redirect('staff_dashboard')  # Replace with actual staff dashboard URL
        else:
            return redirect('adopter_dashboard')  # Redirect to adopter dashboard if the user is not staff
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:
            login(request, user)
            return redirect('staff_dashboard')  # Redirect to the staff dashboard
        else:
            # Provide detailed error messages for invalid credentials or non-staff users
            error = "Invalid credentials or user is not a staff member."
            if user is None:
                error = "Authentication failed. Please check your username and password."
            elif not user.is_staff:
                error = "The logged-in user is not a staff member, but an adopter."

            return render(request, 'staff_login.html', {'error': error})
    
    return render(request, 'staff_login.html')

@login_required
def adopter_dashboard(request):
    if not request.user.is_staff_user:
        adopter_profile = request.user.adopter_profile  # Access adopter profile
        return render(request, 'adopter_dashboard.html', {'profile': adopter_profile})
    else:
        return redirect('staff_login')  # Redirect staff users away

@login_required
def staff_dashboard(request):
    if request.user.is_staff_user:
        staff_profile = request.user.staff_profile  # Access staff profile
        return render(request, 'staff_dashboard.html', {'profile': staff_profile})
    else:
        return redirect('adopter_login')  # Redirect adopters away