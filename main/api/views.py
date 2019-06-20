from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.serializers import (
    OrganizationSerializer,
    DepartmentSerializer,
    EmployeeSerializer,
    StatusSerializer,
    CustomUserSerializer,
)
from api.models import Organization, Department, Employee, Status, CustomUser
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class CustomUserView(viewsets.ModelViewSet):

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    permission_classes = (IsAuthenticated,)


class OrganizationView(viewsets.ModelViewSet):

    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    filter_backends = (filters.OrderingFilter, filters.SearchFilter,
                       DjangoFilterBackend)
    filterset_fields = ('org_name',)
    search_fields = ('org_name', 'dep_count', 'emp_count')
    ordering_fields = ('org_name',)
    ordering = ('org_name',)


class DepartmentView(viewsets.ModelViewSet):

    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    filter_backends = (filters.OrderingFilter, filters.SearchFilter,
                       DjangoFilterBackend)
    filterset_fields = ('organization', 'dep_name')
    search_fields = ('dep_name', 'organization__org_name')
    ordering_fields = ('organization', 'dep_name')
    ordering = ('dep_name', 'organization')


class EmployeeView(viewsets.ModelViewSet):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    filter_backends = (filters.OrderingFilter, filters.SearchFilter,
                       DjangoFilterBackend)
    filterset_fields = ('emp_name',)
    search_fields = ('emp_name', 'department__dep_name', 'status__status_text')
    ordering_fields = ('emp_name', 'department__dep_name',
                       'status__status_text')
    ordering = ('emp_name', 'department__dep_name', 'status__status_text')


class StatusView(viewsets.ModelViewSet):

    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    filter_backends = (filters.OrderingFilter, filters.SearchFilter,
                       DjangoFilterBackend)
    filterset_fields = ('status_text',)
    search_fields = ('status_text',)
    ordering_fields = ('status_text',)
    ordering = ('status_text',)
