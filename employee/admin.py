from django.contrib import admin
from .models import Department, Employee

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department', 'section', 'location')
    list_filter = ('department', 'section', 'location')
    search_fields = ('department', 'section', 'location')

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name_in_arabic', 'name_in_english', 'display_location', 'department', 'job_title_arabic', 'job_title_english', 'marital_status', 'religion', 'national_id', 'expire_date', 'gender', 'date_of_birth', 'place_of_birth')
    list_filter = ('department__location', 'department__department', 'department__section', 'marital_status', 'religion', 'gender')
    search_fields = ('name_in_arabic', 'name_in_english', 'department__department', 'department__section', 'job_title_arabic', 'job_title_english', 'marital_status', 'religion', 'national_id', 'place_of_birth')

    def display_location(self, obj):
        return obj.department.location
    display_location.short_description = 'Location'
    
    
class PersonalInformation(Employee):
    class Meta:
        proxy = True

class PersonalInformationAdmin(admin.ModelAdmin):
    list_display = ('name_in_arabic', 'name_in_english', 'display_location', 'department', 'job_title_arabic', 'job_title_english', 'marital_status', 'religion', 'national_id', 'expire_date', 'gender', 'date_of_birth', 'place_of_birth')
    list_filter = ('department__location', 'department__department', 'department__section', 'marital_status', 'religion', 'gender')
    search_fields = ('name_in_arabic', 'name_in_english', 'department__department', 'department__section', 'job_title_arabic', 'job_title_english', 'marital_status', 'religion', 'national_id', 'place_of_birth')

    def display_location(self, obj):
        return obj.department.location
    display_location.short_description = 'Location'
    
class ContactInformation(Employee):
    class Meta:
        proxy = True

class ContactInformationAdmin(admin.ModelAdmin):
    list_display = ('name_in_arabic', 'name_in_english', 'display_location', 'department', 'job_title_arabic', 'job_title_english', 'marital_status', 'religion', 'national_id', 'expire_date', 'gender', 'date_of_birth', 'place_of_birth')
    list_filter = ('department__location', 'department__department', 'department__section', 'marital_status', 'religion', 'gender')
    search_fields = ('name_in_arabic', 'name_in_english', 'department__department', 'department__section', 'job_title_arabic', 'job_title_english', 'marital_status', 'religion', 'national_id', 'place_of_birth')

    def display_location(self, obj):
        return obj.department.location
    display_location.short_description = 'Location'
    

class Education(Employee):
    class Meta:
        proxy = True

class EducationAdmin(admin.ModelAdmin):
    list_display = ('name_in_arabic', 'name_in_english', 'display_location', 'department', 'job_title_arabic', 'job_title_english', 'marital_status', 'religion', 'national_id', 'expire_date', 'gender', 'date_of_birth', 'place_of_birth')
    list_filter = ('department__location', 'department__department', 'department__section', 'marital_status', 'religion', 'gender')
    search_fields = ('name_in_arabic', 'name_in_english', 'department__department', 'department__section', 'job_title_arabic', 'job_title_english', 'marital_status', 'religion', 'national_id', 'place_of_birth')

    def display_location(self, obj):
        return obj.department.location
    display_location.short_description = 'Location'
    
class InsuranceInformation(Employee):
    class Meta:
        proxy = True

class InsuranceInformationAdmin(admin.ModelAdmin):
    list_display = ('name_in_arabic', 'name_in_english', 'display_location', 'department', 'job_title_arabic', 'job_title_english', 'marital_status', 'religion', 'national_id', 'expire_date', 'gender', 'date_of_birth', 'place_of_birth')
    list_filter = ('department__location', 'department__department', 'department__section', 'marital_status', 'religion', 'gender')
    search_fields = ('name_in_arabic', 'name_in_english', 'department__department', 'department__section', 'job_title_arabic', 'job_title_english', 'marital_status', 'religion', 'national_id', 'place_of_birth')

    def display_location(self, obj):
        return obj.department.location
    display_location.short_description = 'Location'

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(PersonalInformation, PersonalInformationAdmin)
admin.site.register(ContactInformation, ContactInformationAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(InsuranceInformation, InsuranceInformationAdmin)