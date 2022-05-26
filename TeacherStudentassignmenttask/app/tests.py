from django.urls import reverse
from django.test import TestCase
from .models import Teacher, Student, TeacherStudent


class ViewsTestCase(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            first_name="sam",
            last_name="billings",
        )
        self.teacher = Teacher.objects.create(
            first_name="tom",
            last_name="hardy",
        )
        # self.student_techer = TeacherStudent.objects.create(
        #     student=self.student, teacher=self.teacher
        # )

    def test_valid_url(self):
        resp = self.client.get(reverse("home"))
        self.assertEqual(resp.status_code, 200)

    def test_valid_student_add_url(self):
        resp = self.client.get(reverse("student"))
        self.assertEqual(resp.status_code, 200)

    def test_valid_payload_student(self):
        data = self.student
        field_label = data.last_name
        self.assertEqual(field_label, "billings")

    def test_invalid_payload_student(self):
        data = self.student
        field_label = data.last_name
        self.assertHTMLNotEqual(field_label, "sam")

    def test_missing_payload_student(self):
        data = self.student
        field_label = data.last_name
        self.assertHTMLNotEqual(field_label, "")

    def test_update_payload_student(self):
        data = self.student
        data.first_name="shanu"
        data.save()
        field_label = data.first_name
        self.assertEqual(field_label, "shanu")
    
    def test_delete_payload_student(self):
        data = self.student
        id  = data.id
        data.delete()
        try:
            Student.objects.get(id=id)
            self.assertEqual(False, False)
        except:
            self.assertEqual(True, True)

    def test_valid_payload_teacher(self):
        data = self.teacher
        teacher = Teacher.objects.get(id=data.id)
        field_label = teacher.last_name
        self.assertEqual(field_label, "hardy")

    def test_invalid_payload_teacher(self):
        data = self.teacher
        teacher = Teacher.objects.get(id=data.id)
        field_label = teacher.last_name
        self.assertHTMLNotEqual(field_label, "sam")

    def test_missing_payload_teacher(self):
        data = self.teacher
        teacher = Teacher.objects.get(id=data.id)
        field_label = teacher.last_name
        self.assertHTMLNotEqual(field_label, "")

    def test_update_payload_teacher(self):
        data = self.teacher
        data.first_name="john"
        data.save()
        field_label = data.first_name
        self.assertEqual(field_label, "john")
    
    def test_delete_payload_teacher(self):
        data = self.teacher
        id  = data.id
        data.delete()
        try:
            Teacher.objects.get(id=id)
            self.assertEqual(True, False)
        except:
            self.assertEqual(True, True)

    def test_valid_payload_teacher_student(self):
        teacher = self.teacher
        student = self.student
        teacher_student = TeacherStudent.objects.create(
            student=student, teacher=teacher
        )
        field_label = teacher_student.teacher
        self.assertEqual(field_label, teacher)

    def test_invalid_payload_teacher_student(self):
        teacher = self.teacher
        student = self.student
        teacher_student = TeacherStudent.objects.create(
            student=student, teacher=teacher
        )
        field_label = teacher_student.teacher.first_name
        self.assertHTMLNotEqual(field_label, student.first_name)

    def test_missing_payload_teacher_student(self):
        teacher = self.teacher
        student = self.student
        teacher_student = TeacherStudent.objects.create(
            student=student, teacher=teacher
        )
        field_label = teacher_student.teacher.first_name
        self.assertHTMLNotEqual(field_label, student.first_name)

    def assign_student_to_teacher_list(self):
        teacher = self.teacher
        student = self.student
        student_teacher = self.student_techer
        try:
            value = TeacherStudent.objects.get(
                techer=teacher, student = student
            )
            return self.assertEqual(value.id, student_teacher.id)
        except:
            return self.assertEqual(True, False)
    
    def unassigned_student_to_teacher_list(self):
        teacher = self.teacher
        student = self.student
        student_teacher = self.student_techer
        try:
            value = TeacherStudent.objects.get(
                techer=teacher, student = student
            )
            value.delete()
            return self.assertEqual(value.id, student_teacher.id)
        except:
            return self.assertEqual(True, False)

    def mark_as_star_student_to_teacher_list(self):
        teacher = self.teacher
        student = self.student
        teacher_student = TeacherStudent.objects.create(
            teacher=teacher, student=student, 
            is_star=True
        )
        field_label = teacher_student.is_staff
        return self.assertEqual(field_label, True)

    def remove_mark_as_star_student_from_teacher_list(self):
        teacher = self.teacher
        student = self.student
        teacher_student = TeacherStudent.objects.create(
            teacher=teacher, student=student, 
            is_star=True
        )
        teacher_student.is_staff = False
        teacher_student.save()
        field_label = teacher_student.is_staff
        return self.assertEqual(field_label, False)