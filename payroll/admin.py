from django.contrib import admin
from .models import Employee, PayrollPeriod, PayrollEntry

# Register your models here.
admin.site.register(Employee)
admin.site.register(PayrollPeriod)
admin.site.register(PayrollEntry)