from datetime import timezone
from django.db import models

class School(models.Model):
    school_id = models.AutoField(primary_key=True)
    name_th = models.CharField(max_length=255, default=None)
    name_en = models.CharField(max_length=255, default=None)
    address = models.TextField(default=None)
    
    def __str__(self):
        return self.school_id

    class Meta:
        ordering = ['school_id']
        db_table = 'school'


class ClassRoom(models.Model):
    class_room_id = models.AutoField(primary_key=True)
    number_year = models.CharField(max_length=2, default=None)
    slash = models.CharField(max_length=2, default=None)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.class_room_id
    
    class Meta:
        ordering = ['class_room_id']
        db_table = 'class_room'


class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255, default=None)
    last_name = models.CharField(max_length=255, default=None)
    gender = models.CharField(max_length=1, default=None)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.teacher_id
    
    class Meta:
        ordering = ['teacher_id']
        db_table = 'teacher'


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255, default=None)
    last_name = models.CharField(max_length=255, default=None)
    gender = models.CharField(max_length=1, default=None)
    class_room = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.student_id
    
    class Meta:
        ordering = ['student_id']
        db_table = 'student'


class HomeRoom(models.Model):
    home_room_id = models.AutoField(primary_key=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    class_room = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)

    class Meta:
        ordering = ['home_room_id']
        db_table = 'home_room'  