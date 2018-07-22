from django.db import models

class Employee(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  department = models.CharField(max_length=60)

class PayrollPeriod(models.Model):
  start_date = models.DateField()
  end_date = models.DateField()