# Generated by Django 3.2.8 on 2021-12-04 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentApp', '0002_instructor_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='route_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
