# Generated by Django 3.2.8 on 2021-11-11 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentApp', '0011_auto_20211111_0103'),
    ]

    operations = [
        migrations.CreateModel(
            name='timeslot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='department',
            name='building_id',
        ),
        migrations.RemoveField(
            model_name='section',
            name='building_id',
        ),
        migrations.AddField(
            model_name='classroom',
            name='building',
            field=models.CharField(default='Main', max_length=100),
        ),
        migrations.AddField(
            model_name='department',
            name='building',
            field=models.CharField(default='Main', max_length=100),
        ),
        migrations.AddField(
            model_name='section',
            name='building',
            field=models.CharField(default='Main', max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name='classroom',
            unique_together={('building', 'room_no')},
        ),
        migrations.RemoveField(
            model_name='classroom',
            name='building_id',
        ),
        migrations.DeleteModel(
            name='building',
        ),
    ]