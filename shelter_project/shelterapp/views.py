from django.shortcuts import render, redirect, get_object_or_404
from .forms import AnimalForm, AdoptionForm, CombinedAdopterSignupForm, MedicalRecordForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Animal, ShelterLocation, Paycheck, MedicalRecord, Donation, AdoptionRequest, CustomUser, Adopter, Staff
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings

def default_page(request):
    animals = Animal.objects.all()
    return render(request, 'default_page.html', {'animals': animals})

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
    return render(request, 'view_medical_records.html', {'medical_records': medical_records})

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

def user_logout(request):
    logout(request)  # Logs out the user
    return redirect('adopter_login')  # Redirect to login page after logging out

def adopter_signup(request):
    if request.method == 'POST':
        form = CombinedAdopterSignupForm(request.POST)
        if form.is_valid():
            # Create the user with first_name, last_name, and password
            user = form.save()  # The form's save method takes care of user creation

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
            return redirect('staff_dashboard')  # Redirect to the staff dashboard
        else:
            return redirect('adopter_dashboard')  # Redirect to the adopter dashboard

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_staff:
                # Error message for attempting to log into adopter form as staff
                error = "You are trying to log in as a staff member through the adopter login form."
                return render(request, 'adopter_login.html', {'error': error})

            login(request, user)  # Log the adopter user in

            # Check if 'next' is provided in the request and redirect to that URL, otherwise to the dashboard
            next_url = request.POST.get('next')  # Get next from POST (this is passed in the login form)
            if not next_url:
                # Redirect to adopter dashboard
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
            return redirect(settings.STAFF_LOGIN_REDIRECT_URL)
        # Redirect to the user dashboard if the user is not staff
        else:
            return redirect(settings.USER_LOGIN_REDIRECT_URL)

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if not user.is_staff:
                # Error message for attempting to log into staff form as adopter
                error = "You are trying to log in as an adopter through the staff login form."
                return render(request, 'staff_login.html', {'error': error})

            login(request, user)
            # Redirect to the appropriate dashboard based on user type
            if user.is_staff:
                return redirect(settings.STAFF_LOGIN_REDIRECT_URL)  # Redirect to staff dashboard
            else:
                return redirect(settings.USER_LOGIN_REDIRECT_URL)  # Redirect to user dashboard
        else:
            error = "Invalid credentials."
            return render(request, 'staff_login.html', {'error': error})

    return render(request, 'staff_login.html')

def animal_profile(request, animalID):
    animal = get_object_or_404(Animal, animalID=animalID)
    return render(request, 'animal_profile.html', {'animal': animal})


@login_required(login_url='/')  # Redirect unauthenticated users to home page
def adopter_dashboard(request):
    # Check if the user is already on the adopter dashboard
    if request.user.is_staff:
        # Redirect to the staff dashboard if the user is staff
        return redirect('staff_dashboard')  # Replace with actual staff dashboard URL name
    # Otherwise, they are an adopter, so no redirection needed
    return render(request, 'adopter_dashboard.html')

@login_required(login_url='/')  # Redirect unauthenticated users to home page
def staff_dashboard(request):
    # Check if the user is already on the staff dashboard
    if not request.user.is_staff:
        # Redirect to the adopter dashboard if the user is not staff
        return redirect('adopter_dashboard')  # Replace with actual adopter dashboard URL name
    # Otherwise, they are staff, so no redirection needed
    return render(request, 'staff_dashboard.html')
    
@login_required
def adoption_app(request, animalID):
    # Get the logged-in user
    user = request.user

    # Ensure the user has an Adopter profile
    adopter = get_object_or_404(Adopter, adopterID=user.id)

    # Get the specific animal
    animal = get_object_or_404(Animal, animalID=animalID)

    if request.method == 'POST':
        form = AdoptionForm(request.POST)
        if form.is_valid():
            adoption_request = form.save(commit=False)
            adoption_request.adopterID = adopter
            adoption_request.animalID = animal
            adoption_request.save()
            return redirect('adoption_confirmation')
    else:
        form = AdoptionForm()

    return render(request, 'adoption_app.html', {
        'form': form,
        'animal': animal,
    })
    
def adoption_confirmation(request):
    return render(request, 'adoption_confirmation.html')

def add_med_record(request):
    query = request.GET.get('search', '')
    selected_animal = None

    if query:
        animals = Animal.objects.filter(name__icontains=query)  # Search by name
    else:
        animals = Animal.objects.all()  # Default to all animals

    if 'selected_animal' in request.GET:
        selected_animal_id = request.GET.get('selected_animal')
        selected_animal = get_object_or_404(Animal, animalID=selected_animal_id)

    if request.method == 'POST':
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_med_record')  # Redirect to a success page or back to the form
    else:
        form = MedicalRecordForm()

    context = {
        'animals': animals,
        'selected_animal': selected_animal,
        'form': form,
    }
    
    if selected_animal:
        form.initial['animalID'] = selected_animal.animalID
        
    return render(request, 'add_med_record.html', context)

@login_required
def view_adoption_app(request):
    adoption_requests = AdoptionRequest.objects.filter(adopterID=request.user.id).select_related('animalID', 'staffAdministrator')
    
    return render(request, 'view_adoption_app.html', {'adoption_requests': adoption_requests})
