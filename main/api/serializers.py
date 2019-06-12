from rest_framework import serializers
from api.models import Organization, Department, Employee, Status
from django.db.models import Count


# Create your serializers here.


class OrganizationSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='employee-detail')
    emp_name = serializers.StringRelatedField(source='employee.emp_name')
    dep_count = serializers.SerializerMethodField()
    emp_count = serializers.SerializerMethodField()

    class Meta:
        fields = ('org_name', 'dep_count', 'emp_name', 'emp_count', 'url')
        model = Organization

    def get_dep_count(self, obj):
        return Department.objects.filter(organization=obj).count()

    def get_emp_count(self, obj):
        dep = Department.objects.filter(organization=obj)
        return dep.prefetch_related("departments", "departments__employees").count()


class DepartmentSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='department-detail')
    emp_count_for_dep = serializers.SerializerMethodField()
    org_name = serializers.StringRelatedField(source='organization.org_name')

    class Meta:
        fields = ('dep_name', 'org_name', 'emp_count_for_dep',
                  'url', 'organization')
        model = Department

    def get_emp_count_for_dep(self, obj):
        return Employee.objects.filter(department=obj).count()


class EmployeeSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='employee-detail')
    org_name = serializers.StringRelatedField(source='organization.org_name')
    dep_name = serializers.StringRelatedField(source='department.dep_name')
    status_text = serializers.StringRelatedField(source='status.status_text')

    class Meta:
        fields = ('emp_name', 'dep_name', 'org_name', 'status_text',
                  'url', 'department', 'status', )
        model = Employee


class StatusSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='status-detail')
    status_count = serializers.SerializerMethodField()

    class Meta:
        fields = ('status_text', 'status_count', 'url')
        model = Status

    def get_status_count(self, obj):
        return Employee.objects.filter(status=obj).count()
