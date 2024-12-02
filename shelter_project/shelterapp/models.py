from django.db import models

class Staff(models.Model):
    staffID = models.CharField(primary_key=True, max_length=100)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    phoneNumber = models.IntegerField()
    email = models.EmailField()
    hireDate = models.DateField()
    salary = models.IntegerField()
    workLocation = models.IntegerField()
    status = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.firstName} {self.lastName}'


class Adopters(models.Model):
    adopterID = models.CharField(primary_key=True, max_length=100)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    phoneNumber = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.firstName} {self.lastName}'


class Animals(models.Model):
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


class AdoptionRequests(models.Model):
    adoptionID = models.CharField(primary_key=True, max_length=100)
    adopterID = models.ForeignKey(Adopters, on_delete=models.CASCADE)
    animalID = models.ForeignKey(Animals, on_delete=models.CASCADE)
    dateAdopted = models.DateField()
    adoptionStatus = models.CharField(max_length=100)
    staffAdministrator = models.ForeignKey(Staff, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.adopterID} adopting {self.animalID}'


class MedicalRecords(models.Model):
    medicalID = models.AutoField(primary_key=True)
    animalID = models.ForeignKey(Animals, on_delete=models.CASCADE)
    staffID = models.ForeignKey(Staff, on_delete=models.CASCADE)
    diagnosis = models.CharField(max_length=200)
    treatment = models.TextField()
    date = models.DateField()
    note = models.TextField()

    def __str__(self):
        return f'Medical record for {self.animalID}'


class ShelterLocations(models.Model):
    locationID = models.AutoField(primary_key=True)
    locationName = models.CharField(max_length=100)
    address = models.TextField()
    phoneNumber = models.IntegerField()
    capacity = models.IntegerField()
    currentOccupancy = models.IntegerField()
    funds = models.IntegerField()

    def __str__(self):
        return self.locationName


class Donations(models.Model):
    donationID = models.AutoField(primary_key=True)
    locationID = models.ForeignKey(ShelterLocations, on_delete=models.CASCADE)
    amount = models.IntegerField()
    donationDate = models.DateField()
    name = models.CharField(max_length=100)
    phoneNumber = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return f'Donation of {self.amount} by {self.name}'

class Paycheck(models.Model):
    payDate = models.DateField()
    staffID = models.ForeignKey(Staff, on_delete=models.CASCADE)
    hoursWorked = models.IntegerField()
    amount = models.IntegerField()

    class Meta:
        unique_together = ('payDate', 'staffID')

    def __str__(self):
        return f'Paycheck for {self.staffID} on {self.payDate}'
