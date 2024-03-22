from django.contrib import admin
from .models import Location, PersonalInformation

# Register your models here.class LocationAdmin(admin.ModelAdmin):
class LocationAdmin(admin.ModelAdmin):
    list_display = ('location', 'department', 'section')
    list_filter = ('location', 'department', 'section')
    search_fields = ('location', 'department', 'section')

class PersonalInformationAdmin(admin.ModelAdmin):
    list_display = ('Name_in_Arabic', 'Name_in_English', 'display_location', 'section', 'department')

    def display_location(self, obj):
        return obj.location.location
    display_location.short_description = 'Location'
    
    def section(self, obj):
        return obj.location.section
    
    def department(self, obj):
        return obj.location.department

    section.short_description = 'Section'
    department.short_description = 'Department'

    list_filter = ('location__section', 'location__department')
    search_fields = ('Name_in_Arabic', 'Name_in_English', 'location__section', 'location__department')

admin.site.register(Location, LocationAdmin)
admin.site.register(PersonalInformation, PersonalInformationAdmin)