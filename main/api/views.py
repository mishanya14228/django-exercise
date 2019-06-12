from rest_framework import viewsets
from api.serializers import OrganizationSerializer, DepartmentSerializer
from api.serializers import EmployeeSerializer, StatusSerializer
from api.models import Organization, Department, Employee, Status
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class OrganizationView(viewsets.ModelViewSet):

    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    # permission_classes = (AllowAny,)


class DepartmentView(viewsets.ModelViewSet):

    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_backends = (filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend)
    filterset_fields = ('organization', 'dep_name')
    search_fields = ['dep_name']
    ordering_fields = ('organization', 'dep_name')
    ordering = ('dep_name', 'organization')


class EmployeeView(viewsets.ModelViewSet):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class StatusView(viewsets.ModelViewSet):

    queryset = Status.objects.all()
    serializer_class = StatusSerializer
