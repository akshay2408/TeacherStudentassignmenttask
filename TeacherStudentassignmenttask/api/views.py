from rest_framework import viewsets
from .serializers import (
    TeacherSerializer,
    StudentSerializer,
    TeacherStudentSerializer,
)
from .models import Teacher, Student, TeacherStudent

# Create your views here.

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TeacherStudentViewSet(viewsets.ModelViewSet):
    queryset = TeacherStudent.objects.all()
    serializer_class = TeacherStudentSerializer