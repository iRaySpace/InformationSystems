# payroll/views.py
from .models import Employee, PayrollPeriod, PayrollEntry
from rest_framework import viewsets
from .serializers import EmployeeSerializer, PayrollPeriodSerializer, PayrollEntrySerializer

class EmployeeListCreate(viewsets.ModelViewSet):
  queryset = Employee.objects.all()
  serializer_class = EmployeeSerializer

class PayrollPeriodListCreate(viewsets.ModelViewSet):
  queryset = PayrollPeriod.objects.all()
  serializer_class = PayrollPeriodSerializer

class PayrollEntryListCreate(viewsets.ModelViewSet):
  queryset = PayrollEntry.objects.all()
  serializer_class = PayrollEntrySerializer