# Generated by Django 5.0.6 on 2024-09-07 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_delete_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='Financial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=200, null=True)),
                ('passport_path', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
