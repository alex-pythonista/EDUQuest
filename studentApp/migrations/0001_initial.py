# Generated by Django 3.2.8 on 2021-11-10 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(default='', max_length=10)),
                ('title', models.CharField(default='', max_length=200)),
                ('dept_name', models.CharField(default='', max_length=10)),
                ('credit', models.IntegerField(default=3)),
            ],
        ),
    ]