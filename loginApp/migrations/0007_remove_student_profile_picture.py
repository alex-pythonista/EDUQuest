# Generated by Django 3.2.8 on 2021-11-24 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginApp', '0006_student_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='profile_picture',
        ),
    ]