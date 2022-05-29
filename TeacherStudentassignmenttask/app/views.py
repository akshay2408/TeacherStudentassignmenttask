from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.db.models import Q
from django.forms import modelform_factory
from django.contrib import messages
from .models import Teacher, Student, TeacherStudent


def home(request):
    return render(request, "app/home.html")


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


class AddStudent(CreateView):
    template_name = "app/student.html"
    model = Student
    fields = ["first_name", "last_name"]
    success_url = reverse_lazy("student")

    def form_valid(self, form):
        return super(AddStudent, self).form_valid(form)


class StudentList(ListView):
    model = Student
    template_name = "app/student_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UpdateStudent(UpdateView):
    model = Student
    template_name = "app/update_student.html"
    fields = ["first_name", "last_name"]
    success_url = reverse_lazy("student_list")

    def update_student(request, pk):
        student = get_object_or_404(Student, id=pk)


class DeleteStudent(DeleteView):
    model = Student
    template_name = "app/delete_student.html"
    success_url = reverse_lazy("student_list")

    def delete_teacher(request, pk):
        student = get_object_or_404(Student, id=pk)


class AssignedTeacherStudentList(ListView):
    model = TeacherStudent
    template_name = "app/assigned_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UpdateAssignedTeacherStudent(UpdateView):
    model = TeacherStudent
    template_name = "app/update_assigned_list.html"
    fields = ["teacher", "student", "is_star"]
    success_url = reverse_lazy("assigned_list")

    def update_assigned_list(request, pk):
        assigned_list = get_object_or_404(TeacherStudent, id=pk)


class DeleteAssignedTeacherStudent(DeleteView):
    model = TeacherStudent
    template_name = "app/delete_assigned_list.html"
    success_url = reverse_lazy("assigned_list")

    def delete_assigned_list(request, pk):
        student = get_object_or_404(TeacherStudent, id=pk)


def assigned_students(request, pk):
    student_obj = TeacherStudent.objects.filter(teacher=pk).select_related(
        "teacher", "student"
    )
    teacher = getattr(student_obj.first(), "teacher", None)
    context = {"teacher": teacher, "student": student_obj}
    return render(request, "app/select_student.html", context)


def unassigned_students(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    ids = teacher.teacher.values_list("student_id", flat=True)
    students = Student.objects.filter(~Q(id__in=ids))
    context = {"teacher": teacher, "students": students}
    return render(request, "app/select_unsigned_student.html", context)


def add_student(request, teacher, student):
    try:
        student = Student.objects.get(id=student)
        teacher = Teacher.objects.get(id=teacher)
        TeacherStudent.objects.get_or_create(teacher=teacher, student=student)
        messages.add_message(
            request,
            messages.SUCCESS,
            f"Student has been added in your student list.",
        )
    except:
        messages.add_message(request, messages.ERROR, "somthing goes wrong")
    return redirect("unassigned_students", teacher.id)


def remove_student(request, teacher, student):
    record = TeacherStudent.objects.get(teacher=teacher, student=student)
    record.delete()
    messages.add_message(
        request,
        messages.SUCCESS,
        f"Student removed in your student list.",
    )
    return redirect("selected_student", teacher)


def mark_as_star(request, teacher, student):
    relation_object = TeacherStudent.objects.filter(teacher=teacher, student=student)
    is_star = False if relation_object[0].is_star else True
    relation_object.update(is_star=is_star)
    messages.add_message(
        request,
        messages.SUCCESS,
        f"Student updated",
    )
    return redirect("selected_student", teacher)
