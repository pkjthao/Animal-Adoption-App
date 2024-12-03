from django.urls import path
from . import views

urlpatterns = [
    path('', views.default_page, name='default_page'),  # Main page with options
    path('submit/', views.submit_animal, name='submit_animal'),  # Submit animal form
    path('animals/', views.view_animals, name='view_animals'),  # View list of animals
    path('adoption/', views.adoption_app, name='adoption_app'),
    # View list of shelter locations
    path('shelter_locations/', views.view_shelters, name='view_shelters'),
    # View list of paychecks
    path('staff_paychecks/', views.view_paychecks, name='view_paychecks'),
    # View list of medical records
    path('medical_records/', views.view_medical_records, name='view_medical_records'),
    # View list of employees
    path('employees/', views.view_employees, name='view_employees')
]
