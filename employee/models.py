from django.db import models

# Create your models here.

class Location(models.Model):
    location = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    section = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.section} ({self.department}, {self.location})"

class PersonalInformation(models.Model):
    Name_in_Arabic = models.CharField(max_length=100, unique=True)
    Name_in_English = models.CharField(max_length=100, unique=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Name_in_Arabic} / {self.Name_in_English}"
    
