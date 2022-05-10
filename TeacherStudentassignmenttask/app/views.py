from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import Teacher, Student, TeacherStudent
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView


def home(request):
    return render(request, 'app/home.html')


class AddTeacher(CreateView):
    template_name = "app/teacher.html"
    model = Teacher
    fields = ["first_name", "last_name"]
    success_url = reverse_lazy("teacher")

    def form_valid(self, form):
        return super(AddTeacher, self).form_valid(form)


class TeacherList(ListView):
    model = Teacher
    template_name = "app/teacher_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UpdateTeacher(UpdateView):
    model = Teacher
    template_name = "app/update_teacher.html"
    fields = ["first_name", "last_name"]
    success_url = reverse_lazy("teacher_list")

    def update_teacher(request, pk):
        teacher = get_object_or_404(Teacher, id=pk)


class DeleteTeacher(DeleteView):
    model = Teacher
    template_name = "app/delete_teacher.html"
    success_url = reverse_lazy("teacher_list")

    def delete_teacher(request, pk):
        teacher = get_object_or_404(Teacher, id=pk)



