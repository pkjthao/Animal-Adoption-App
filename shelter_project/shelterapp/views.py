from django.shortcuts import render, redirect
from .forms import AnimalForm
from .forms import AdoptionForm
from .models import Animals, ShelterLocations, Paycheck, MedicalRecords
from .models import AdoptionRequests

def submit_animal(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('animal_list')  # Redirect to the list page
    else:
        form = AnimalForm()

    return render(request, 'submit_animal.html', {'form': form})

def view_animals(request):
    animals = Animals.objects.all()
    return render(request, 'view_animals.html', {'animals': animals})

def view_shelters(request):
    shelters = ShelterLocations.objects.all()
    return render(request, 'view_shelters.html', {'shelters': shelters})

def view_paychecks(request):
    paychecks = Paycheck.objects.all()
    return render(request, 'view_paychecks.html', {'paychecks': paychecks})

def view_medical_records(request):
    medical_records = MedicalRecords.objects.all()
    animals = Animals.objects.all()
    return render(request, 'view_medical_records.html', {'medical_records': medical_records, 'animals': animals})

def default_page(request):
    return render(request, 'default_page.html')

def adoption_app(request):
    if request.method == 'POST':
        form = AdoptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adoption_app')
    else:
        form = AnimalForm()
    
    return render(request, 'adoption_app.html', {'form': form})