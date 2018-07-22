# payroll/urls.py
from django.urls import path

from . import views

urlpatterns = [
  path('api/payroll_period/', views.PayrollPeriodListCreate.as_view()),
  path('api/employee/', views.EmployeeListCreate.as_view())
]