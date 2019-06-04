from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.


class Organization(models.Model):
    org_name = models.CharField(max_length=100)

    def slug(self):
        return slugify(self.org_name)

    def __str__(self):
        return self.org_name


class Department(models.Model):
    dep_name = models.CharField(max_length=100)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def slug(self):
        return slugify(self.dep_name)

    def __str__(self):
        return self.dep_name


class Employee(models.Model):
    emp_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    status_choices = (
        ('1', 'Manager'),
        ('2', 'Developer'),
        ('3', 'Boss')
    )
    status = models.CharField(max_length=1, choices=status_choices)

    def slug(self):
        return slugify(self.emp_name)

    def __str__(self):
        return self.emp_name
