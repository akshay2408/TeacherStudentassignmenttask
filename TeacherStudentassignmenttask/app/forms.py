from django import forms


class StudentForm(forms.Form):
    student_field = forms.BooleanField()
