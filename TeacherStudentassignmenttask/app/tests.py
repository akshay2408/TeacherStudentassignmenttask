import traceback
from django.urls import reverse
from django.test import TestCase
from .models import Teacher, Student, TeacherStudent


class ViewsTestCase(TestCase):
    def setUp(self):
        self.first_name = "shan"
        self.last_name = "rai"

        self.tc_obj = {
             "first_name": "shan",
            "last_name": "rai"
        }
        self.teacher = Teacher.objects.create(
            first_name=self.first_name,
            last_name=self.last_name
            )
        self.student = Student.objects.create(
            first_name=self.first_name,
            last_name=self.last_name
            )

    def add_student_url(self,teacher_id, student_id):
        return reverse(
            "add_student",
            kwargs={"teacher": teacher_id,
                    "student":student_id
            })

    def test_valid_url(self):
        resp = self.client.get(reverse("home"))
        self.assertEqual(resp.status_code, 200)

    def test_valid_teacher_list_url(self):
        resp = self.client.get(reverse("teacher_list"))
        self.assertEqual(resp.status_code, 200)

    def test_add_teacher(self):
        resp = self.client.get(
            reverse("teacher"),
            args=[self.first_name, self.last_name]
        )
        self.assertEqual(resp.status_code, 200)

    def test_update_teacher(self):
        teacher = self.teacher
        url = reverse(
            "update_teacher",
            kwargs={"pk": teacher.id}
            )

        payload = {
            "first_name": "ndk",
            "last_name": teacher.last_name
            }
        resp = self.client.post(url, payload)

        teacher_obj = Teacher.objects.filter(
            first_name=payload.get("first_name")
            )
        resp_code = resp.status_code

        self.assertEqual(resp_code, 302)
        self.assertNotEqual(teacher_obj, None)

    def test_delete_teacher(self):
        teacher = self.teacher
        url = reverse(
            "delete_teacher",
            kwargs={"pk": teacher.id}
            )
        resp = self.client.post(url)
        resp_code = resp.status_code
        self.assertEqual(resp_code, 302)
        teacher_obj = list(Teacher.objects.filter(
            id=teacher.id
            ))
        self.assertEqual(teacher_obj, list())

    def test_valid_student_list_url(self):
        resp = self.client.get(reverse("student_list"))
        self.assertEqual(resp.status_code, 200)

    def test_add_student(self):
        resp = self.client.get(reverse(
            "student"),
            args=[
                self.first_name,
                self.last_name
            ])
        self.assertEqual(resp.status_code, 200)

    def test_update_student(self):
        student = self.student
        url = reverse(
            "update_student",
            kwargs={"pk": student.id}
            )

        payload = {
            "first_name": "csk",
            "last_name": student.last_name
            }
        resp = self.client.post(url, payload)

        teacher_obj = Student.objects.filter(
            first_name=payload.get("first_name")
            )
        resp_code = resp.status_code

        self.assertEqual(resp_code, 302)
        self.assertNotEqual(teacher_obj, None)

    def test_delete_student(self):
        student = self.student
        url = reverse(
            "delete_student",
            kwargs={"pk": student.id}
            )
        resp = self.client.post(url)
        resp_code = resp.status_code
        self.assertEqual(resp_code, 302)
        teacher_obj = list(Student.objects.filter(
            id=student.id
            ))
        self.assertEqual(teacher_obj, list())

    def test_valid_assigned_list_url(self):
        resp = self.client.get(reverse("assigned_list"))
        self.assertEqual(resp.status_code, 200)

    def test_valid_teacher_assigned_student_url(self):
        teacher = self.teacher
        url = reverse(
            "selected_student",
            kwargs={"pk": teacher.id}
            )
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_valid_teacher_unassigned_student_url(self):
        teacher = self.teacher
        url = reverse(
            "unassigned_students",
            kwargs={"pk": teacher.id}
            )
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_add_student_to_teacher_list(self):
        teacher = self.teacher
        student = self.student
        url = self.add_student_url(teacher.id, student.id)
        resp = self.client.get(url)
        teacher_studet_obj = TeacherStudent.objects.filter(
            teacher=teacher,
            student=student
        ).first()
        self.assertNotEqual(teacher_studet_obj, None)

    def test_remove_student_to_teacher_list(self):
        teacher = self.teacher
        student = self.student
        url = self.add_student_url(teacher.id, student.id)
        resp = self.client.get(url)
        url = reverse(
            "remove_student",
            kwargs={"teacher": teacher.id,
                    "student":student.id
            })
        resp = self.client.get(url)
        teacher_studet_obj = TeacherStudent.objects.filter(
            teacher=teacher,
            student=student
        ).first()
        self.assertEqual(teacher_studet_obj, None)

    def test_mark_as_star_student(self):
        teacher = self.teacher
        student = self.student
        url = self.add_student_url(teacher.id, student.id)
        resp = self.client.get(url)
        url = reverse(
            "mark_as_star",
            kwargs={"teacher": teacher.id,
                    "student":student.id
            })
        resp = self.client.get(url)
        teacher_studet_star_obj = TeacherStudent.objects.filter(
            teacher=teacher,
            student=student
        ).first()
        url = reverse(
            "mark_as_star",
            kwargs={"teacher": teacher.id,
                    "student":student.id
            })
        resp = self.client.get(url)
        teacher_studet_remove_star_obj = TeacherStudent.objects.filter(
            teacher=teacher,
            student=student
        ).first()
        self.assertEqual(teacher_studet_star_obj.is_star, True)
        self.assertEqual(teacher_studet_remove_star_obj.is_star, False)