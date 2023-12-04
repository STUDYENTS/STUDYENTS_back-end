# Generated by Django 4.2.6 on 2023-10-16 02:52

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('course_description', models.TextField(default='This is the default content.')),
                ('author', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='images/')),
                ('courses', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('alias', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('theory', models.TextField(default='This is the default content.')),
                ('video', models.FileField(upload_to='theory_files/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])])),
                ('file', models.FileField(upload_to='theory_files/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])])),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('number_of_tasks', models.IntegerField()),
                ('number_of_completed_tasks', models.IntegerField()),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapi.lesson')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=100)),
                ('correct_answer', models.CharField(max_length=100)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapi.test')),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('number_of_tasks', models.IntegerField()),
                ('number_of_tests', models.IntegerField()),
                ('number_of_completed_tasks', models.IntegerField()),
                ('number_of_completed_tests', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapi.course')),
            ],
        ),
        migrations.AddField(
            model_name='lesson',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapi.module'),
        ),
        migrations.CreateModel(
            name='IncorrectAnswers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('answer', models.CharField(max_length=100)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapi.task')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='courses',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapi.courses'),
        ),
    ]
