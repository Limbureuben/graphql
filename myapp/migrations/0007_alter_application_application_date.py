# Generated by Django 5.0.6 on 2024-09-01 19:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_application_application_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='application_date',
            field=models.DateTimeField(blank=True, default=datetime.date.today, null=True),
        ),
    ]
