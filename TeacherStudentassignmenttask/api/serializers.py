from rest_framework import serializers
from .models import Teacher, Student, TeacherStudent


class TeacherSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name']


class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'teacher']


class TeacherStudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TeacherStudent
        fields = ['teacher', 'student', 'is_star']