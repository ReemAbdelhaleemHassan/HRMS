from django.db import models

class Department(models.Model):
    department = models.CharField(max_length=100, null=True)
    section = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100, null=True)
    department_manager = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True, related_name='managed_department')

class Employee(models.Model):
    RELIGION_CHOICES = [
        ('Muslim', 'Muslim'),
        ('Christian', 'Christian'),
    ]

    MARITAL_STATUS_CHOICES = [
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
        ('Widow', 'Widow'),
    ]

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    name_in_arabic = models.CharField(max_length=100)
    name_in_english = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    job_title_arabic = models.CharField(max_length=100, null=True)
    job_title_english = models.CharField(max_length=100, null=True)
    marital_status = models.CharField(max_length=50, choices=MARITAL_STATUS_CHOICES, null=True)
    religion = models.CharField(max_length=50, choices=RELIGION_CHOICES, null=True)
    national_id = models.CharField(max_length=50, null=True)
    expire_date = models.DateField(null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True)
    date_of_birth = models.DateField(null=True)
    place_of_birth = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    address = models.TextField(null=True)
    work_phone = models.CharField(max_length=20, null=True)
    mobile_no = models.CharField(max_length=20, null=True)
    education = models.CharField(max_length=100, null=True)
    military_status = models.CharField(max_length=50, null=True)
    direct_manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)
    join_date = models.DateField(null=True)
    hiring_date = models.DateField(null=True)
    contract_type = models.CharField(max_length=100, null=True)
    contract_start_date = models.DateField(null=True)
    contract_end_date = models.DateField(null=True)
    bank_name = models.CharField(max_length=100, null=True)
    bank_account_no = models.CharField(max_length=100, null=True)
    insurance_type = models.CharField(max_length=100, null=True)
    insurance_no = models.CharField(max_length=100, null=True)
    insurance_branch = models.CharField(max_length=100, null=True)
    private_health_insurance = models.BooleanField(null=True)
    previous_insurance_years = models.IntegerField(null=True)
    previous_insurance_months = models.IntegerField(null=True)