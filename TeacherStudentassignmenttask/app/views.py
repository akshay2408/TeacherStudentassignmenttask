from multiprocessing import context
from django import forms
from .forms import StudentForm
from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import Teacher, Student, TeacherStudent
from django.urls import reverse_lazy
# from django.forms import ModelForm
from django.views.generic.edit import DeleteView
from django.db.models import Q
from django.forms import modelform_factory
from django.contrib import messages


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


# class AssignTeacher(CreateView):
#     model = TeacherStudent
#     template_name = "app/assign_teacher.html"
#     form_class = StudentAddForm
#     success_url = reverse_lazy("assign_teacher")
    
#     # def get_form_kwargs(self):
#     #     print(self.kwargs)
#     #     self.student = Student.objects.all()
#     #     kwargs = super().get_form_kwargs()
#     #     kwargs['student'] = self.student
#     #     return kwargs
    
#     def form_valid(self, form):
#         form.instance.student = self.student
#         return super(AssignTeacher, self).form_valid(form)

#     def get_context_data(self, **kwargs):
#         self.id = self.request.GET.get('id')
#         context = super(AssignTeacher, self).get_context_data(**kwargs)
#         context['teacher_obj'] = Teacher.objects.get(id=self.id)
#         return context
    

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
        

def selected_student(request,pk):
    teacher=Teacher.objects.get(pk=pk)
    student_obj = TeacherStudent.objects.filter(Q(teacher_id=pk))
    context={'teacher':teacher,'student':student_obj}
    return render(request,"app/select_student.html",context)


def unsigned_student(request,pk):
    teacher=Teacher.objects.get(pk=pk)
    ids = teacher.teacher1.values_list('student_id', flat=True)
    students = Student.objects.filter(~Q(id__in = ids))
    context={'teacher':teacher,'students':students}
    return render(request,"app/select_unsigned_student.html",context)


# def studentform(request):
    
#     studentformset=modelform_factory(TeacherStudent,fields='__all__')
#     formset = studentformset()
#     context={
#         'formset':formset
#     }
#     return render(request,'app/studentform.html',context)
    
# def addstudent(request,pk):
#     return render(request,'app/studentform.html')

# def studentselect(request):
    
#     context ={}
#     form = StudentForm()
#     context['form']= form
#     if request.GET:
#         temp = request.GET['student_field']
#         print(temp)
#     return render( request, "app/studentform.html", context)

# def selectstudent(request,pk):
#     teacher=Teacher.objects.get(pk=pk)
#     ids = teacher.teacher1.values_list('student_id', flat=True)
#     students = Student.objects.filter(~Q(id__in = ids))
#     context={'teacher':teacher,'students':students,}
#     Student = Student.objects.get(id=pk)
#     print(Student)
    # import pdb;pdb.set_trace()
    # wish_list, created = Wishlist.objects.get_or_create(
    #     product=product, user=request.user
    # )

    # messages.info(request, "The item was added to your wishlist")
    # return redirect("shop:index")

def add_student(request, teacher, student):
    try:
        student = Student.objects.get(id=student)
        teacher = Teacher.objects.get(id=teacher)
        TeacherStudent.objects.get_or_create(
            teacher=teacher,
            student=student
        )
        messages.add_message(
            request,
            messages.SUCCESS,
            f'Student {student.first_name} {student.last_name} has been added in your student list.')
    except:
        messages.add_message(request, messages.ERROR, 'Something went wrong.')
    return redirect('unsigned_student', teacher.id)


def mark_as_star(request, teacher, student):
    try:
        student = Student.objects.get(id=student)
        relation_object = TeacherStudent.objects.filter(
            teacher=teacher,
            student=student
        )
        is_star = False if relation_object[0].is_star else True
        relation_object.update(is_star=is_star)
        messages.add_message(
            request,
            messages.SUCCESS,
            f'Student {student.first_name} {student.last_name} updated')
    except:
        messages.add_message(request, messages.ERROR, 'Something went wrong.')
    return redirect('selected_student', teacher)
