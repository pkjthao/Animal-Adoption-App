from django.shortcuts import render, redirect
from .forms import AnimalForm
from .forms import AdoptionForm
from .models import Animals
from .models import AdoptionRequests

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
    animals = Animals.objects.all()
    medical_records = medical_records.objects.all()
    return render(request, 'view_animals.html', {'animals': animals, 'medical_records': medical_records})

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