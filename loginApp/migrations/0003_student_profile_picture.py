# Generated by Django 3.2.8 on 2021-11-30 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginApp', '0002_auto_20211130_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='student_profile'),
        ),
    ]