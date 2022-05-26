from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from .schema import schema

urlpatterns = [
    path("", views.home, name="home"),
    path("teacher", views.AddTeacher.as_view(), name="teacher"),
    path("teacher_list", views.TeacherList.as_view(), name="teacher_list"),
    path(
        "update_teacher/<int:pk>", views.UpdateTeacher.as_view(), name="update_teacher"
    ),
    path(
        "delete_teacher/<int:pk>", views.DeleteTeacher.as_view(), name="delete_teacher"
    ),
    path("student", views.AddStudent.as_view(), name="student"),
    path("student_list", views.StudentList.as_view(), name="student_list"),
    path(
        "student_teacher/<int:pk>", views.UpdateStudent.as_view(), name="update_student"
    ),
    path(
        "delete_student/<int:pk>", views.DeleteStudent.as_view(), name="delete_student"
    ),
    # path("assign_teacher/", views.AssignTeacher.as_view(), name="assign_teacher"),
    path(
        "assigned_list",
        views.AssignedTeacherStudentList.as_view(),
        name="assigned_list",
    ),
    path(
        "update_assigned_list/<int:pk>",
        views.UpdateAssignedTeacherStudent.as_view(),
        name="update_assigned_list",
    ),
    path(
        "delete_assigned_list/<int:pk>",
        views.DeleteAssignedTeacherStudent.as_view(),
        name="delete_assigned_list",
    ),
    path("selected_student/<int:pk>", views.assigned_students, name="selected_student"),
    path(
        "unassigned_students/<int:pk>",
        views.unassigned_students,
        name="unassigned_students",
    ),
    path(
        "add-student/<int:teacher>/<int:student>/",
        views.add_student,
        name="add_student",
    ),
    path(
        "remove_student/<int:teacher>/<int:student>/",
        views.remove_student,
        name="remove_student",
    ),
    path(
        "mark-as-star/<int:teacher>/<int:student>/",
        views.mark_as_star,
        name="mark_as_star",
    ),
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),   
   ]
