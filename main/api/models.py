from django.db import models

# Create your models here.


class Organization(models.Model):
    org_name = models.CharField(max_length=100)

    def __str__(self):
        return self.org_name


class Department(models.Model):
    dep_name = models.CharField(max_length=100)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE,
                                     related_name='departments')

    def __str__(self):
        return self.dep_name


class Status(models.Model):
    status_text = models.CharField(max_length=100)

    def __str__(self):
        return self.status_text


class Employee(models.Model):
    emp_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,
                                   related_name='employees')
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.emp_name
