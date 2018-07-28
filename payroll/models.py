from django.db import models

class Employee(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  department = models.CharField(max_length=60)

  def __str__(self):
    return "%s %s/%s" % (self.first_name, self.last_name, self.department)

class PayrollPeriod(models.Model):
  name = models.CharField(max_length=30)
  start_date = models.DateField()
  end_date = models.DateField()

  def __str__(self):
    return "%s/%s-%s" % (self.name, self.start_date, self.end_date)

class PayrollEntry(models.Model):
  payroll_period = models.ForeignKey(PayrollPeriod, on_delete=models.CASCADE)
  employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
  number_of_hours = models.IntegerField()

  def __str__(self):
    return "%s/%s" % (self.payroll_period, self.employee)