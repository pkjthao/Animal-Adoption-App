from django.urls import path
from . import views

urlpatterns = [
    path('', views.default_page, name='default_page'),  # Main page with options
    path('submit/', views.submit_animal, name='submit_animal'),  # Submit animal form
    path('animals/', views.view_animals, name='view_animals'),  # View list of animals
    path('adoption/', views.adoption_app, name='adoption_app')
]
