from django.contrib import admin
from .models import Location, PersonalInformation, ContactInformation

# Register your models here.class LocationAdmin(admin.ModelAdmin):
class PersonalInformationAdmin(admin.ModelAdmin):
    list_display = ('Name_in_Arabic', 'Name_in_English', 'display_location', 'section', 'department', 'marital_status', 'religion', 'national_id', 'expire_date', 'gender', 'date_of_birth', 'place_of_birth')

    def display_location(self, obj):
        return obj.location.location
    display_location.short_description = 'Location'
    
    def section(self, obj):
        return obj.location.section
    
    def department(self, obj):
        return obj.location.department

    section.short_description = 'Section'
    department.short_description = 'Department'

    list_filter = ('location__section', 'location__department', 'marital_status', 'religion', 'gender')
    search_fields = ('Name_in_Arabic', 'Name_in_English', 'location__section', 'location__department', 'marital_status', 'religion', 'national_id', 'place_of_birth')


class ContactInformationAdmin(admin.ModelAdmin):
    list_display = ('get_employee_name', 'email_address', 'address', 'work_phone', 'mobile_no')
    # list_filter = ('employee__employee_name',)  # Filter by employee name
    search_fields = ('employee__employee_name', 'email_address')  # Enable searching by employee name and email address

    def get_employee_name(self, obj):
        return obj.employee.Name_in_English
    get_employee_name.short_description = 'Employee Name'
    
    
class LocationAdmin(admin.ModelAdmin):
    list_display = ('location', 'department', 'section')
    list_filter = ('location', 'department', 'section')
    search_fields = ('location', 'department', 'section')
    
    
admin.site.register(Location, LocationAdmin)
admin.site.register(PersonalInformation, PersonalInformationAdmin)    
admin.site.register(ContactInformation, ContactInformationAdmin)