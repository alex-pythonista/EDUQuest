# Generated by Django 3.2.8 on 2021-11-11 01:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentApp', '0010_alter_department_building_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='room_no',
            field=models.ForeignKey(default='Not assigned', on_delete=django.db.models.deletion.DO_NOTHING, to='studentApp.classroom'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='department',
            name='building_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='studentApp.building'),
        ),
        migrations.AlterUniqueTogether(
            name='section',
            unique_together={('course_id', 'section_id', 'sem_code')},
        ),
    ]
