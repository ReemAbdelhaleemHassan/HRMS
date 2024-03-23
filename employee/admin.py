from django.contrib import admin
from .models import Department, Employee
from django.db.models import Count
from column_toggle.admin import ColumnToggleModelAdmin


@admin.register(Department)
class DepartmentAdmin(ColumnToggleModelAdmin):
    default_selected_columns = ['department', 'section', 'location', 'department_manager', 'get_department_manager_id', 
                    'employees_count']
    autocomplete_fields = ['department_manager']
    list_display = ['department', 'section', 'location', 'department_manager', 'get_department_manager_id', 
                    'employees_count']
    list_editable = ['department_manager']
    list_per_page = 10
    list_filter = ['department', 'section', 'location']
    search_fields = ['department', 'section', 'location', 'department_manager__name_in_english']
    list_select_related = ['department_manager']
    
    def get_department_manager_id(self, department):
        manager = department.department_manager
        if manager:
            return manager.id
        return None
    
    def employees_count(self, department):
        return department.employees_count
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(employees_count=Count('employee'))


class EmployeeAdmin(ColumnToggleModelAdmin):
    autocomplete_fields = ['department']
    raw_id_fields = ['direct_manager']
    default_selected_columns = ['id', 'name_in_arabic', 'name_in_english', 'display_location', 'department', 'display_section', 
                    'job_title_arabic', 'job_title_english', 'marital_status', 'religion', 'national_id', 
                    'expire_date', 'gender', 'date_of_birth', 'place_of_birth', 'email', 'address', 'work_phone',
                    'mobile_no', 'education', 'military_status', 'direct_manager', 'join_date', 'hiring_date', 
                    'contract_type', 'contract_start_date', 'contract_end_date', 'bank_name', 'bank_account_no',
                    'insurance_type', 'insurance_no', 'insurance_branch', 'private_health_insurance', 
                    'previous_insurance_years', 'previous_insurance_months']
    list_display = ['id', 'name_in_arabic', 'name_in_english', 'display_location', 'department', 'display_section', 
                    'job_title_arabic', 'job_title_english', 'marital_status', 'religion', 'national_id', 
                    'expire_date', 'gender', 'date_of_birth', 'place_of_birth', 'email', 'address', 'work_phone',
                    'mobile_no', 'education', 'military_status', 'direct_manager', 'join_date', 'hiring_date', 
                    'contract_type', 'contract_start_date', 'contract_end_date', 'bank_name', 'bank_account_no',
                    'insurance_type', 'insurance_no', 'insurance_branch', 'private_health_insurance', 
                    'previous_insurance_years', 'previous_insurance_months']
    list_per_page = 10
    list_filter = ['department__location', 'department__department', 'department__section', 'job_title_arabic', 
                    'job_title_english', 'marital_status', 'religion', 'expire_date', 'gender', 'date_of_birth', 
                    'place_of_birth', 'education', 'military_status', 'direct_manager', 'join_date', 'hiring_date', 
                    'contract_type', 'contract_start_date', 'contract_end_date', 'bank_name', 'insurance_type', 
                    'insurance_branch', 'private_health_insurance', 'previous_insurance_years', 
                    'previous_insurance_months']
    search_fields = ['id', 'name_in_arabic', 'name_in_english', 'department__location', 'department__department',
                    'department__section',
                    'job_title_arabic', 'job_title_english', 'marital_status', 'religion', 'national_id', 
                    'expire_date', 'gender', 'date_of_birth', 'place_of_birth', 'email', 'address', 'work_phone',
                    'mobile_no', 'education', 'military_status', 'direct_manager__name_in_english', 
                    'direct_manager__id', 'join_date', 'hiring_date', 
                    'contract_type', 'contract_start_date', 'contract_end_date', 'bank_name', 'bank_account_no',
                    'insurance_type', 'insurance_no', 'insurance_branch', 'private_health_insurance', 
                    'previous_insurance_years', 'previous_insurance_months']

    def display_location(self, obj):
        return obj.department.location
    display_location.short_description = 'Location'
    
    def display_section(self, obj):
        return obj.department.section
    display_section.short_description = 'section'
    
    
class PersonalInformation(Employee):
    class Meta:
        proxy = True

class PersonalInformationAdmin(ColumnToggleModelAdmin):
    default_selected_columns = ['id', 'name_in_arabic', 'name_in_english', 'display_location', 'department', 'display_section', 
                    'job_title_arabic', 'job_title_english', 'marital_status', 'religion', 'national_id', 
                    'expire_date', 'gender', 'date_of_birth', 'place_of_birth']
    list_display = ['id', 'name_in_arabic', 'name_in_english', 'display_location', 'department', 'display_section', 
                    'job_title_arabic', 'job_title_english', 'marital_status', 'religion', 'national_id', 
                    'expire_date', 'gender', 'date_of_birth', 'place_of_birth']
    list_per_page = 10
    list_filter = ['department__location', 'department__department', 'department__section', 'job_title_arabic', 
                    'job_title_english', 'marital_status', 'religion', 'expire_date', 'gender', 'date_of_birth', 
                    'place_of_birth']
    search_fields = ['id', 'name_in_arabic', 'name_in_english', 'department__location', 'department__department', 
                    'department__section',
                    'job_title_arabic', 'job_title_english', 'marital_status', 'religion', 'national_id', 
                    'expire_date', 'gender', 'date_of_birth', 'place_of_birth']
    
    def has_add_permission(self, request):
        return False

    def display_location(self, obj):
        return obj.department.location
    display_location.short_description = 'Location'
    
    def display_section(self, obj):
        return obj.department.section
    display_section.short_description = 'section'
    
class ContactInformation(Employee):
    class Meta:
        proxy = True

class ContactInformationAdmin(ColumnToggleModelAdmin):
    default_selected_columns = ['id', 'name_in_arabic', 'name_in_english', 'email', 'address', 'work_phone', 'mobile_no']
    list_display = ['id', 'name_in_arabic', 'name_in_english', 'email', 'address', 'work_phone', 'mobile_no']
    list_per_page = 10
    search_fields = ['id', 'name_in_arabic', 'name_in_english', 'email', 'address', 'work_phone', 'mobile_no']
    
    def has_add_permission(self, request):
        return False

    def display_location(self, obj):
        return obj.department.location
    display_location.short_description = 'Location'
    
    def display_section(self, obj):
        return obj.department.section
    display_section.short_description = 'section'
    

class Education(Employee):
    class Meta:
        proxy = True

class EducationAdmin(ColumnToggleModelAdmin):
    default_selected_columns = ['id', 'name_in_arabic', 'name_in_english', 'education', 'military_status', 'direct_manager']
    list_display = ['id', 'name_in_arabic', 'name_in_english', 'education', 'military_status', 'direct_manager']
    raw_id_fields = ['direct_manager']
    list_per_page = 10
    list_filter = ['education', 'military_status', 'direct_manager']
    search_fields = ['id', 'name_in_arabic', 'name_in_english', 'education', 'military_status', 
                    'direct_manager__name_in_english', 
                    'direct_manager__id',]
    
    def has_add_permission(self, request):
        return False

    def display_location(self, obj):
        return obj.department.location
    display_location.short_description = 'Location'
    
    def display_section(self, obj):
        return obj.department.section
    display_section.short_description = 'section'
    
class InsuranceInformation(Employee):
    class Meta:
        proxy = True
class InsuranceInformationAdmin(ColumnToggleModelAdmin):
    default_selected_columns = ['id', 'name_in_arabic', 'name_in_english', 'join_date', 'hiring_date', 
                    'contract_type', 'contract_start_date', 'contract_end_date', 'bank_name', 'bank_account_no',
                    'insurance_type', 'insurance_no', 'insurance_branch', 'private_health_insurance', 
                    'previous_insurance_years', 'previous_insurance_months']
    list_display = ['id', 'name_in_arabic', 'name_in_english', 'join_date', 'hiring_date', 
                    'contract_type', 'contract_start_date', 'contract_end_date', 'bank_name', 'bank_account_no',
                    'insurance_type', 'insurance_no', 'insurance_branch', 'private_health_insurance', 
                    'previous_insurance_years', 'previous_insurance_months']
    list_per_page = 10
    list_filter = ['join_date', 'hiring_date', 'contract_type', 'contract_start_date', 'contract_end_date', 
                    'bank_name', 'insurance_type', 'insurance_branch', 'private_health_insurance', 
                    'previous_insurance_years', 'previous_insurance_months']
    search_fields = ['id', 'name_in_arabic', 'name_in_english', 'join_date', 'hiring_date', 
                    'contract_type', 'contract_start_date', 'contract_end_date', 'bank_name', 'bank_account_no',
                    'insurance_type', 'insurance_no', 'insurance_branch', 'private_health_insurance', 
                    'previous_insurance_years', 'previous_insurance_months']
    
    def has_add_permission(self, request):
        return False

    def display_location(self, obj):
        return obj.department.location
    display_location.short_description = 'Location'
    
    def display_section(self, obj):
        return obj.department.section
    display_section.short_description = 'section'


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(PersonalInformation, PersonalInformationAdmin)
admin.site.register(ContactInformation, ContactInformationAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(InsuranceInformation, InsuranceInformationAdmin)