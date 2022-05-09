from django.db import models

# Create your models here.


class Teacher(models.Model):
    name = models.ManyToManyField(to='teacher', blank=True, null=True)


class Student(models.Model):
    name = models.ManyToManyField(to='student', blank=True, null=True)


class TeacherStudent(models.Model):
    teacher = models.ForeignKey(to='teacher',on_delete=models.CASCADE, blank=True, null=True)
    Student = models.ForeignKey(to='student', on_delete=models.CASCADE, blank=True, null=True)
    is_star = models.BooleanField(default=False, blank=True, null=True)