# payroll/urls.py
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register("employees", views.EmployeeListCreate)
router.register("payroll_periods", views.PayrollPeriodListCreate)
router.register("payroll_entries", views.PayrollEntryListCreate)

urlpatterns = router.urls