# Generated by Django 3.2.8 on 2021-11-11 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentApp', '0008_auto_20211111_0031'),
    ]

    operations = [
        migrations.CreateModel(
            name='building',
            fields=[
                ('building_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('building_name', models.CharField(default='Main', max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='department',
            name='building',
        ),
        migrations.AlterField(
            model_name='classroom',
            name='room_no',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='course',
            name='dept_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='studentApp.department'),
        ),
        migrations.AlterField(
            model_name='inst_degree',
            name='inst_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='studentApp.instructor'),
        ),
        migrations.AlterField(
            model_name='inst_field',
            name='inst_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='studentApp.instructor'),
        ),
        migrations.AlterField(
            model_name='inst_publication',
            name='inst_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='studentApp.instructor'),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='dept_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='studentApp.department'),
        ),
        migrations.CreateModel(
            name='section',
            fields=[
                ('section_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('sem_code', models.CharField(max_length=4)),
                ('building_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='studentApp.building')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='studentApp.course')),
            ],
        ),
        migrations.AddField(
            model_name='classroom',
            name='building_id',
            field=models.ForeignKey(default='Not assigned', on_delete=django.db.models.deletion.DO_NOTHING, to='studentApp.building'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='department',
            name='building_id',
            field=models.ForeignKey(default='Not assigned', on_delete=django.db.models.deletion.DO_NOTHING, to='studentApp.building'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='classroom',
            unique_together={('building_id', 'room_no')},
        ),
        migrations.RemoveField(
            model_name='classroom',
            name='building',
        ),
    ]