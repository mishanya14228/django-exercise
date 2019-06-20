from django.contrib import admin
from .models import Organization, Department, Employee, Status, CustomUser
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

# Register your models here.


class CustomUserAdmin(UserAdmin):
    # The forms to add and change user instances

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference the removed 'username' field
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)


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
    list_display = ('emp_name', 'department', 'status')


admin.site.register(Employee, MyEmployeeAdmin)


class MyStatusAdmin(admin.ModelAdmin):
    model = Status
    list_display = ('status_text',)


admin.site.register(Status, MyStatusAdmin)
