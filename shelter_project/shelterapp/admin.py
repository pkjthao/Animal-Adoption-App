from django.contrib import admin
from .models import Staff, Adopters, Animals, AdoptionRequests, MedicalRecords, ShelterLocations, Donations, Paycheck

admin.site.register(Staff)
admin.site.register(Adopters)
admin.site.register(Animals)
admin.site.register(AdoptionRequests)
admin.site.register(MedicalRecords)
admin.site.register(ShelterLocations)
admin.site.register(Donations)
admin.site.register(Paycheck)
