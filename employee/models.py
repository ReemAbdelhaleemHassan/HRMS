from django.db import models

# Create your models here.

class Location(models.Model):
    location = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    section = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.section} ({self.department}, {self.location})"

class PersonalInformation(models.Model):
    MARITAL_STATUS_CHOICES = [
        ('single', 'Single'),
        ('married', 'Married'),
        ('divorced', 'Divorced'),
        ('widow', 'Widow'),
    ]

    RELIGION_CHOICES = [
        ('muslim', 'Muslim'),
        ('christian', 'Christian'),
    ]

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    Name_in_Arabic = models.CharField(max_length=100, unique=True)
    Name_in_English = models.CharField(max_length=100, unique=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS_CHOICES, null=True)
    religion = models.CharField(max_length=10, choices=RELIGION_CHOICES, null=True)
    national_id = models.CharField(max_length=14, unique=True, null=True)
    expire_date = models.DateField(null=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True)
    date_of_birth = models.DateField(null=True) 
    place_of_birth = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.Name_in_Arabic} / {self.Name_in_English}"
    
class ContactInformation(models.Model):
    # Define your fields in the ContactInformation model
    employee = models.ForeignKey(PersonalInformation, on_delete=models.CASCADE, primary_key=True)
    email_address = models.EmailField(null=True)
    address = models.CharField(max_length=255)
    work_phone = models.CharField(max_length=20, null=True)
    mobile_no = models.CharField(max_length=20)