from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Staff, Adopter, Animal, AdoptionRequest, MedicalRecord, ShelterLocation, Donation, Paycheck, CustomUser

admin.site.register(Staff)
admin.site.register(Adopter)
admin.site.register(Animal)
admin.site.register(AdoptionRequest)
admin.site.register(MedicalRecord)
admin.site.register(ShelterLocation)
admin.site.register(Donation)
admin.site.register(Paycheck)

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    pass