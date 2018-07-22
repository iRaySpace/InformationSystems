# payroll/views.py
from .models import Employee, PayrollPeriod
from rest_framework import generics
from .serializers import EmployeeSerializer, PayrollPeriodSerializer

class EmployeeListCreate(generics.ListCreateAPIView):
  queryset = Employee.objects.all()
  serializer_class = EmployeeSerializer

class PayrollPeriodListCreate(generics.ListCreateAPIView):
  queryset = PayrollPeriod.objects.all()
  serializer_class = PayrollPeriodSerializer