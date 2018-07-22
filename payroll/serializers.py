from .models import Employee, PayrollPeriod
from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Employee
    fields= ('first_name', 'last_name', 'department')

class PayrollPeriodSerializer(serializers.ModelSerializer):
  class Meta:
    model = PayrollPeriod
    fields = ('start_date', 'end_date')