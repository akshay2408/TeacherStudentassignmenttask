from graphene_django import DjangoObjectType
from .models import *
import graphene


class TeacherType(DjangoObjectType):
    class Meta:
        model = Teacher
        fields = "__all__"


class StudentType(DjangoObjectType):
    class Meta:
        model = Student
        fields = "__all__"


class Query(graphene.ObjectType):

    all_students = graphene.List(StudentType)
    all_teacher = graphene.List(TeacherType)

    def resolve_all_students(root, info):
        return Student.objects.all()

    def resolve_all_teacher(root, info):
        return Teacher.objects.all()


schema = graphene.Schema(query=Query)
