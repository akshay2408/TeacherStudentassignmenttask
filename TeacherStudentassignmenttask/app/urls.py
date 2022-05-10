from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('teacher', views.AddTeacher.as_view(), name='teacher'),
    path('teacher_list', views.TeacherList.as_view(), name='teacher_list'),
    path('update_teacher/<int:pk>', views.UpdateTeacher.as_view(), name='update_teacher'),
    path('delete_teacher/<int:pk>', views.DeleteTeacher.as_view(), name='delete_teacher'),
    path('student', views.AddStudent.as_view(), name='student'),
    path('student_list', views.StudentList.as_view(), name='student_list'),
    path('student_teacher/<int:pk>', views.UpdateStudent.as_view(), name='update_student'),
    path('delete_student/<int:pk>', views.DeleteStudent.as_view(), name='delete_student'),
]
