# Generated by Django 3.2.8 on 2021-11-30 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loginApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('building_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('building_name', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'building',
            },
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.IntegerField()),
                ('capacity', models.IntegerField(blank=True, null=True)),
                ('building_id', models.ForeignKey(db_column='building_id', on_delete=django.db.models.deletion.DO_NOTHING, to='studentApp.building')),
            ],
            options={
                'db_table': 'classroom',
                'unique_together': {('building_id', 'room_no')},
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('credits', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
            ],
            options={
                'db_table': 'course',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('building_id', models.ForeignKey(blank=True, db_column='building_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='studentApp.building')),
            ],
            options={
                'db_table': 'department',
            },
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('inst_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('designation', models.CharField(blank=True, max_length=100, null=True)),
                ('dept_name', models.ForeignKey(blank=True, db_column='dept_name', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='studentApp.department')),
            ],
            options={
                'db_table': 'instructor',
            },
        ),
        migrations.CreateModel(
            name='Timeslot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeslot_id', models.CharField(max_length=10)),
                ('day', models.CharField(max_length=5)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'timeslot',
                'unique_together': {('timeslot_id', 'day', 'start_time')},
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_id', models.IntegerField()),
                ('sem_code', models.CharField(max_length=8)),
                ('building_id', models.ForeignKey(db_column='building_id', on_delete=django.db.models.deletion.DO_NOTHING, related_name='section_classroom_buildingno', to='studentApp.building')),
                ('course_id', models.ForeignKey(db_column='course_id', on_delete=django.db.models.deletion.DO_NOTHING, to='studentApp.course')),
                ('room_no', models.ForeignKey(db_column='room_no', on_delete=django.db.models.deletion.DO_NOTHING, related_name='section_classroom_roomno', to='studentApp.classroom')),
                ('timeslot_id', models.ForeignKey(db_column='timeslot_id', on_delete=django.db.models.deletion.DO_NOTHING, to='studentApp.timeslot')),
            ],
            options={
                'db_table': 'section',
                'unique_together': {('course_id', 'section_id', 'sem_code')},
            },
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('route_id', models.AutoField(primary_key=True, serialize=False)),
                ('route_name', models.CharField(blank=True, max_length=100, null=True)),
                ('shuttle_id', models.CharField(blank=True, max_length=5, null=True)),
                ('remark', models.CharField(blank=True, max_length=200, null=True)),
                ('timeslot_id', models.ForeignKey(blank=True, db_column='timeslot_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='studentApp.timeslot')),
            ],
            options={
                'db_table': 'route',
            },
        ),
        migrations.CreateModel(
            name='InstPublication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(blank=True, max_length=500, null=True)),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('journal', models.CharField(blank=True, max_length=200, null=True)),
                ('publication_year', models.CharField(blank=True, max_length=4, null=True)),
                ('inst_id', models.ForeignKey(db_column='inst_id', on_delete=django.db.models.deletion.DO_NOTHING, to='studentApp.instructor')),
            ],
            options={
                'db_table': 'inst_publication',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='dept_name',
            field=models.ForeignKey(blank=True, db_column='dept_name', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='studentApp.department'),
        ),
        migrations.CreateModel(
            name='StudentCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ct1', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('ct2', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('ct3', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('quiz', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('assignment1', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('assignment2', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('mid', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('grade', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('course_id', models.ForeignKey(db_column='course_id', on_delete=django.db.models.deletion.DO_NOTHING, related_name='studentcourse_section_courseid', to='studentApp.course')),
                ('section_id', models.ForeignKey(db_column='section_id', on_delete=django.db.models.deletion.DO_NOTHING, related_name='studentcourse_section_sectionid', to='studentApp.section')),
                ('sem_code', models.ForeignKey(db_column='sem_code', on_delete=django.db.models.deletion.DO_NOTHING, related_name='studentcourse_semcode', to='studentApp.section')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='loginApp.student')),
            ],
            options={
                'db_table': 'student_course',
                'unique_together': {('student_id', 'course_id', 'section_id', 'sem_code')},
            },
        ),
        migrations.CreateModel(
            name='Prereq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='prereq_course_course', to='studentApp.course')),
                ('prereq_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='prereq_course_prereq', to='studentApp.course')),
            ],
            options={
                'db_table': 'prereq',
                'unique_together': {('course_id', 'prereq_id')},
            },
        ),
        migrations.CreateModel(
            name='InstTeaches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.ForeignKey(db_column='course_id', on_delete=django.db.models.deletion.DO_NOTHING, related_name='instteaches_section_courseid', to='studentApp.course')),
                ('inst_id', models.ForeignKey(db_column='inst_id', on_delete=django.db.models.deletion.DO_NOTHING, to='studentApp.instructor')),
                ('section_id', models.ForeignKey(db_column='section_id', on_delete=django.db.models.deletion.DO_NOTHING, related_name='instteaches_section_sectionid', to='studentApp.section')),
                ('sem_code', models.ForeignKey(db_column='sem_code', on_delete=django.db.models.deletion.DO_NOTHING, related_name='instteaches_semcode', to='studentApp.section')),
            ],
            options={
                'db_table': 'inst_teaches',
                'unique_together': {('inst_id', 'course_id', 'section_id', 'sem_code')},
            },
        ),
        migrations.CreateModel(
            name='InstField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_of_interest', models.CharField(max_length=50)),
                ('inst_id', models.ForeignKey(db_column='inst_id', on_delete=django.db.models.deletion.DO_NOTHING, to='studentApp.instructor')),
            ],
            options={
                'db_table': 'inst_field',
                'unique_together': {('inst_id', 'field_of_interest')},
            },
        ),
        migrations.CreateModel(
            name='InstDegree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree_name', models.CharField(max_length=200)),
                ('institution', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=100)),
                ('degree_year', models.CharField(max_length=4)),
                ('inst_id', models.ForeignKey(db_column='inst_id', on_delete=django.db.models.deletion.DO_NOTHING, to='studentApp.instructor')),
            ],
            options={
                'db_table': 'inst_degree',
                'unique_together': {('inst_id', 'degree_name', 'institution', 'country', 'degree_year')},
            },
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_id', models.CharField(max_length=5)),
                ('driver_name', models.CharField(max_length=100)),
                ('route_id', models.ForeignKey(db_column='route_id', on_delete=django.db.models.deletion.DO_NOTHING, to='studentApp.route')),
            ],
            options={
                'db_table': 'driver',
                'unique_together': {('driver_id', 'driver_name', 'route_id')},
            },
        ),
    ]
