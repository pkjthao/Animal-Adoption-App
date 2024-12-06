from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.default_page, name='default_page'),
    #path('home/', views.default_page, name='default_page'),# Main page with options
    path('submit/', views.submit_animal, name='submit_animal'),  # Submit animal form
    path('animals/', views.view_animals, name='view_animals'),  # View list of animals
    #path('adoption/', views.adoption_app, name='adoption_app'),
    # View list of shelter locations
    path('shelter_locations/', views.view_shelters, name='view_shelters'),
    # View list of paychecks
    path('staff_paychecks/', views.view_paychecks, name='view_paychecks'),
    # View list of medical records
    #path('view_medical_records/', views.view_medical_records, name='view_medical_records'),
    # View donations
    path('donations/', views.view_donations, name='view_donations'),
    # Medical record search
    path('medical-records/', views.medical_records_search, name='medical_records_search'),
    # Staff login (no signup option)
    path('staff/login/', auth_views.LoginView.as_view(template_name='staff_login.html'), name='staff_login'),
    path('animal/<int:animalID>/', views.animal_profile, name='animal_profile'),
    path('adopt/<int:animalID>/', views.adoption_app, name='adoption_app'),
    path('medical-request/', views.add_med_record, name='add_med_record'),
    path('adoption-apps/', views.view_adoption_app, name='view_adoption_app')
]

urlpatterns += [
    path('view_medical_records/', views.view_medical_records, name='view_medical_records'),
    # View list of employees
    path('employees/', views.view_employees, name='view_employees')
]

# All Staff + Adopter Sign ups and Logins
urlpatterns += [
    path('user/login/', views.adopter_login, name='adopter_login'),
    path('staff/login/', views.staff_login, name='staff_login'),
    path('adopter/signup/', views.adopter_signup, name='adopter_signup'),
    path('adopter/dashboard/', views.adopter_dashboard, name='adopter_dashboard'),
    path('staff/dashboard/', views.staff_dashboard, name='staff_dashboard'),
    path('logout/', views.user_logout, name='user_logout'),
    path('profile/', views.profile_view, name='profile_view')
]

# Edit Forms
urlpatterns += [
    path('edit_adoption_request/', views.edit_adoption_request, name='edit_adoption_request'),
    path('edit_medical_record/', views.edit_medical_record, name='edit_medical_record'),
]