from .models import Employee, PayrollPeriod, PayrollEntry
from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Employee
    fields = '__all__'

class PayrollPeriodSerializer(serializers.ModelSerializer):
  class Meta:
    model = PayrollPeriod
    fields = '__all__'

class PayrollEntrySerializer(serializers.ModelSerializer):
  class Meta:
    model = PayrollEntry
    fields = '__all__'