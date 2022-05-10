from django.db import models

# Create your models here.


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name}"
    

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    teacher = models.ManyToManyField(Teacher)

    def __str__(self):
        return f"{self.first_name}"


class TeacherStudent(models.Model):
    teacher = models.ForeignKey(to='teacher',on_delete=models.CASCADE)
    student = models.ForeignKey(to='student', on_delete=models.CASCADE)
    is_star = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.teacher}"