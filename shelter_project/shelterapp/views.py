from django.shortcuts import render, redirect
from .forms import AnimalForm
from .models import Animals

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

def default_page(request):
    return render(request, 'default_page.html')