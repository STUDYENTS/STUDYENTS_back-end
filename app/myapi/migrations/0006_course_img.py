# Generated by Django 4.2.6 on 2023-12-15 04:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0005_alter_test_number_of_completed_tasks_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='img',
            field=models.FileField(blank=True, null=True, upload_to='img_course/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'svg', 'gpg'])]),
        ),
    ]