from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('teacher', views.AddTeacher.as_view(), name='teacher'),
    path('teacher_list', views.TeacherList.as_view(), name='teacher_list'),
    path('update_teacher/<int:pk>', views.UpdateTeacher.as_view(), name='update_teacher'),
    path('delete_teacher/<int:pk>', views.DeleteTeacher.as_view(), name='delete_teacher'),
]
