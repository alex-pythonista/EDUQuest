# Generated by Django 3.2.8 on 2021-11-29 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentApp', '0017_alter_studentcourse_course_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='driver_id',
            field=models.CharField(max_length=5),
        ),
    ]
