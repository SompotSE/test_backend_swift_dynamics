# Generated by Django 5.0.4 on 2024-07-02 04:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeRoomTeacher',
            fields=[
                ('home_room_id', models.AutoField(primary_key=True, serialize=False)),
                ('teacher_code', models.CharField(max_length=50)),
                ('class_room_code', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'home_room_teacher',
                'ordering': ['home_room_id'],
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('school_id', models.AutoField(primary_key=True, serialize=False)),
                ('name_th', models.CharField(default=None, max_length=255)),
                ('name_en', models.CharField(default=None, max_length=255)),
                ('address', models.TextField(default=None)),
            ],
            options={
                'db_table': 'school',
                'ordering': ['school_id'],
            },
        ),
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('class_room_id', models.AutoField(primary_key=True, serialize=False)),
                ('number_year', models.CharField(default=None, max_length=2)),
                ('slash', models.CharField(default=None, max_length=2)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.school')),
            ],
            options={
                'db_table': 'class_room',
                'ordering': ['class_room_id'],
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(default=None, max_length=255)),
                ('last_name', models.CharField(default=None, max_length=255)),
                ('gender', models.CharField(default=None, max_length=1)),
                ('classroom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='apis.classroom')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='apis.school')),
            ],
            options={
                'db_table': 'student',
                'ordering': ['student_id'],
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(default=None, max_length=255)),
                ('last_name', models.CharField(default=None, max_length=255)),
                ('gender', models.CharField(default=None, max_length=1)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='apis.school')),
            ],
            options={
                'db_table': 'teacher',
                'ordering': ['teacher_id'],
            },
        ),
    ]