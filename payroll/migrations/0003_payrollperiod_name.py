# Generated by Django 2.0.7 on 2018-07-23 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0002_payrollentry'),
    ]

    operations = [
        migrations.AddField(
            model_name='payrollperiod',
            name='name',
            field=models.CharField(default='Period', max_length=30),
            preserve_default=False,
        ),
    ]
