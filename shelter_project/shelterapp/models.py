from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)

class CustomUser(AbstractUser):
    objects = CustomUserManager()  # Ensure the custom manager is assigned
    is_staff_user = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Staff(models.Model):
    staffID = models.AutoField(primary_key=True, unique=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='staff_profile')
    position = models.CharField(max_length=100)
    phone_number = models.CharField(
        max_length=14,  # Adjusted for (XXX) XXX-XXXX format
        validators=[
            RegexValidator(
                regex=r'^\(\d{3}\) \d{3}-\d{4}$',
                message="Phone number must be in the format '(XXX) XXX-XXXX'."
            )
        ]
    )
    hireDate = models.DateField()
    salary = models.IntegerField()

    def __str__(self):
        return f'{self.user.username} - {self.position}'


class Adopter(models.Model):
    adopterID = models.AutoField(primary_key=True, unique=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='adopter_profile')
    phone_number = models.CharField(
        max_length=14,
        validators=[
            RegexValidator(
                regex=r'^\(\d{3}\) \d{3}-\d{4}$',
                message="Phone number must be in the format '(XXX) XXX-XXXX'."
            )
        ]
    )
    address = models.TextField()

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class ShelterLocation(models.Model):
    locationID = models.AutoField(primary_key=True)
    locationName = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(
        max_length=14,
        validators=[
            RegexValidator(
                regex=r'^\(\d{3}\) \d{3}-\d{4}$',
                message="Phone number must be in the format '(XXX) XXX-XXXX'."
            )
        ]
    )
    capacity = models.IntegerField()
    currentOccupancy = models.IntegerField()
    funds = models.IntegerField()

    def __str__(self):
        return self.locationName


class Donation(models.Model):
    donationID = models.AutoField(primary_key=True)
    locationID = models.ForeignKey(ShelterLocation, on_delete=models.CASCADE)
    amount = models.IntegerField()
    donationDate = models.DateField()
    name = models.CharField(max_length=100)
    phone_number = models.CharField(
        max_length=14,
        validators=[
            RegexValidator(
                regex=r'^\(\d{3}\) \d{3}-\d{4}$',
                message="Phone number must be in the format '(XXX) XXX-XXXX'."
            )
        ]
    )
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return f'Donation of {self.amount} by {self.name}'



class Animal(models.Model):
    animalID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    dateOfArrival = models.DateField()
    adoptedOrNot = models.IntegerField()
    healthStatus = models.CharField(max_length=100)
    description = models.TextField()
    locationID = models.IntegerField()
    reasonForIntake = models.CharField(max_length=100)
    adoptionFee = models.IntegerField()

    def __str__(self):
        return self.name


class AdoptionRequest(models.Model):
    adoptionID = models.CharField(primary_key=True, max_length=100)
    adopterID = models.ForeignKey(Adopter, on_delete=models.CASCADE)
    animalID = models.ForeignKey(Animal, on_delete=models.CASCADE)
    dateAdopted = models.DateField()
    adoptionStatus = models.CharField(max_length=100)
    staffAdministrator = models.ForeignKey(Staff, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.adopterID} adopting {self.animalID}'


class MedicalRecord(models.Model):
    medicalID = models.AutoField(primary_key=True)
    animalID = models.ForeignKey(Animal, on_delete=models.CASCADE)
    staffID = models.ForeignKey(Staff, on_delete=models.CASCADE)
    diagnosis = models.CharField(max_length=200)
    treatment = models.TextField()
    date = models.DateField()
    note = models.TextField()

    def __str__(self):
        return f'Medical record for {self.animalID}'

class Paycheck(models.Model):
    payDate = models.DateField()
    staffID = models.ForeignKey(Staff, on_delete=models.CASCADE)
    hoursWorked = models.IntegerField()
    amount = models.IntegerField()

    class Meta:
        unique_together = ('payDate', 'staffID')

    def __str__(self):
        return f'Paycheck for {self.staffID} on {self.payDate}'
    