from rest_framework import serializers
from api.models import Organization, Department, Employee, Status


# Create your serializers here.


class OrganizationSerializer(serializers.ModelSerializer):
    dep_count = serializers.SerializerMethodField()
    emp_count = serializers.SerializerMethodField()

    class Meta:
        model = Organization
        fields = '__all__'

    def get_dep_count(self, obj):
        return Department.objects.filter(organization=obj).count()

    def get_emp_count(self, obj):
        dep = Department.objects.filter(organization=obj)
        return dep.prefetch_related("departments", "departments__employees").count()


class DescriptionOrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = ("id", "org_name")


class DepartmentSerializer(serializers.ModelSerializer):
    emp_count_for_dep = serializers.SerializerMethodField()
    organization = DescriptionOrganizationSerializer()

    class Meta:
        model = Department
        fields = '__all__'


    def get_emp_count_for_dep(self, obj):
        return Employee.objects.filter(department=obj).count()


class StatusSerializer(serializers.ModelSerializer):
    status_count = serializers.SerializerMethodField()

    class Meta:
        model = Status
        fields = '__all__'

    def get_status_count(self, obj):
        return Employee.objects.filter(status=obj).count()


class DescriptionDepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ("id", "dep_name")


class DescriptionStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = ("id", "status_text")


class EmployeeSerializer(serializers.ModelSerializer):
    department = DescriptionDepartmentSerializer()
    status = DescriptionStatusSerializer()

    class Meta:
        model = Employee
        fields = '__all__'
