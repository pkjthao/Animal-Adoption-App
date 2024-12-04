from django.shortcuts import render, redirect
from .forms import AnimalForm, AdoptionForm, CustomUserCreationForm, MedicalRecordForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Animal, ShelterLocation, Paycheck, MedicalRecord, AdoptionRequest, CustomUser, Adopter
from django.shortcuts import render, get_object_or_404

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

def view_medical_records(request):
    medical_records = MedicalRecord.objects.all()
    animals = Animal.objects.all()
    return render(request, 'view_medical_records.html', {'medical_records': medical_records, 'animals': animals})

def default_page(request):
    return render(request, 'default_page.html')

# def adoption_app(request):
#     if request.method == 'POST':
#         form = AdoptionForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('adoption_app')
#     else:
#         form = AdoptionForm()
    
#     return render(request, 'adoption_app.html', {'form': form})

def user_signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'user_signup.html', {'form': form})

def animal_profile(request, animalID):
    animal = get_object_or_404(Animal, animalID=animalID)
    return render(request, 'animal_profile.html', {'animal': animal})

@login_required
def after_login(request):
    if request.user.is_staff_user:
        return redirect('staff_dashboard')  # Replace with your staff dashboard URL
    else:
        return redirect('user_dashboard')  # Replace with your user dashboard URL
    
@login_required
def adoption_app(request, animalID):
    # Get the logged-in user
    user = request.user

    # Ensure the user has an Adopter profile
    adopter = get_object_or_404(Adopter, email=user.email)

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