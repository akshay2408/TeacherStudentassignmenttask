from django.db import models

# Create your models here.


class Teacher(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)


class Student(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    teacher = models.ManyToManyField(Teacher)


class TeacherStudent(models.Model):
    teacher = models.ForeignKey(to='teacher',on_delete=models.CASCADE, blank=True, null=True)
    Student = models.ForeignKey(to='student', on_delete=models.CASCADE, blank=True, null=True)
    is_star = models.BooleanField(default=False, blank=True, null=True)