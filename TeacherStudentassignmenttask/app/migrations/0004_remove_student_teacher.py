# Generated by Django 4.0.4 on 2022-05-10 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_student_first_name_alter_student_last_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='teacher',
        ),
    ]