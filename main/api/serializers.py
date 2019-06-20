from rest_framework import serializers
from api.models import Organization, Department, Employee, Status, CustomUser


# Create your serializers here.


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = '__all__'


class OrganizationSerializer(serializers.ModelSerializer):
    dep_count = serializers.SerializerMethodField()
    emp_count = serializers.SerializerMethodField()

    class Meta:
        model = Organization
        fields = '__all__'

    def get_dep_count(self, obj):
        return Department.objects.filter(organization=obj).count()

    def get_emp_count(self, obj):
        return Employee.objects.filter(department__organization=obj).count()


class DescriptionOrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = ("id", "org_name")


class DepartmentSerializer(serializers.ModelSerializer):
    emp_count_for_dep = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['organization'] = DescriptionOrganizationSerializer(
                                  instance.organization
                              ).data
        return rep


    def get_emp_count_for_dep(self, obj):
        return Employee.objects.filter(department=obj).count()


class StatusSerializer(serializers.ModelSerializer):
    emp_count_for_status = serializers.SerializerMethodField()

    class Meta:
        model = Status
        fields = '__all__'

    def get_emp_count_for_status(self, obj):
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

    class Meta:
        model = Employee
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['department'] = DescriptionDepartmentSerializer(
                                instance.department
                            ).data
        rep['status'] = DescriptionStatusSerializer(instance.status).data
        return rep
