from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Staff, Adopter, Animal, AdoptionRequest, MedicalRecord, ShelterLocation, Donation, Paycheck, CustomUser
from .forms import StaffAdminForm

# Use custom StaffAdmin for Staff model
class StaffAdmin(admin.ModelAdmin):
    form = StaffAdminForm

    # Customize list display and filtering in admin interface
    list_display = ['user', 'position', 'phone_number', 'hireDate', 'salary']
    search_fields = ['user__username', 'position', 'phone_number']
    list_filter = ['hireDate']

    def save_model(self, request, obj, form, change):
        # Ensure the CustomUser is created/updated when saving the Staff instance
        form.save()
        super().save_model(request, obj, form, change)

# Register all models
admin.site.register(Staff, StaffAdmin)  # Use StaffAdmin for Staff model
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