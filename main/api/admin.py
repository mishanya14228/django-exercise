from django.contrib import admin
from .models import Organization, Department, Employee, Status

# Register your models here.


class MyOrganizationAdmin(admin.ModelAdmin):
    model = Organization
    list_display = ('org_name',)


admin.site.register(Organization, MyOrganizationAdmin)


class MyDepartmentAdmin(admin.ModelAdmin):
    model = Department
    list_display = ('dep_name', 'organization')


admin.site.register(Department, MyDepartmentAdmin)


class MyEmployeeAdmin(admin.ModelAdmin):
    model = Employee
    list_display = ('emp_name', 'department')


admin.site.register(Employee, MyEmployeeAdmin)


class MyStatusAdmin(admin.ModelAdmin):
    model = Status
    list_display = ('status_text',)


admin.site.register(Status, MyStatusAdmin)
