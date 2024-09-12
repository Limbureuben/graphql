# Generated by Django 5.0.6 on 2024-09-03 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_application_application_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(default='', max_length=55)),
                ('employ_status', models.CharField(default='', max_length=255)),
                ('details_month', models.CharField(default='', max_length=255)),
                ('employ_name', models.CharField(default='', max_length=255)),
                ('profile_picture', models.FileField(upload_to='media/')),
            ],
        ),
    ]
