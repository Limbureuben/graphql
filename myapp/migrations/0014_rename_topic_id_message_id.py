# Generated by Django 5.0.6 on 2024-09-15 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='topic_id',
            new_name='id',
        ),
    ]
