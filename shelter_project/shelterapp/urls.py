from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.default_page, name='default_page'),  # Main page with options
    path('submit/', views.submit_animal, name='submit_animal'),  # Submit animal form
    path('animals/', views.view_animals, name='view_animals'),  # View list of animals
    path('adoption/', views.adoption_app, name='adoption_app'),
    path('add/user/', views.add_adopters, name='add_adopters'),
    # View list of shelter locations
    path('shelter_locations/', views.view_shelters, name='view_shelters'),
    # View list of paychecks
    path('staff_paychecks/', views.view_paychecks, name='view_paychecks'),
    # View list of medical records
    path('medical_records/', views.view_medical_records, name='view_medical_records'),
    # View donations
    path('donations/', views.view_donations, name='view_donations'),
    #User login and signup
    path('user/login/', auth_views.LoginView.as_view(template_name='user_login.html'), name='user_login'),
    path('user/signup/', views.user_signup, name='user_signup'),
    # Staff login (no signup option)
    path('staff/login/', auth_views.LoginView.as_view(template_name='staff_login.html'), name='staff_login'),
    # Medical record search
    path('medical-records/', views.medical_records_search, name='medical_records_search')
]

urlpatterns += [
    path('accounts/profile/', views.after_login),  # Default login redirect
    path('medical_records/', views.view_medical_records, name='view_medical_records'),
    # View list of employees
    path('employees/', views.view_employees, name='view_employees')
]
