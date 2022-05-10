from django.contrib import admin
from .models import Teacher, Student, TeacherStudent


# Register your models here.

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(TeacherStudent)