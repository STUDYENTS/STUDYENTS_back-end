# Generated by Django 4.2.6 on 2023-11-03 00:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0004_alter_module_number_of_tests'),
    ]

    operations = [
        migrations.RenameField(
            model_name='module',
            old_name='number_of_completed_tasks',
            new_name='number_of_completed_tests',
        ),
    ]
