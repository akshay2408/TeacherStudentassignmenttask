from django.db import models

# Create your models here.


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + " " + self.last_name


class TeacherStudent(models.Model):
    teacher = models.ForeignKey(to="teacher", on_delete=models.CASCADE, related_name="teacher")
    student = models.ForeignKey(to="student", on_delete=models.CASCADE, related_name="student")
    is_star = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.teacher} : {self.student}"
