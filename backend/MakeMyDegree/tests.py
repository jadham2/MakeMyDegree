from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from MakeMyDegree.models import *


class UserTests(APITestCase):
    def setUp(self):
        compe_degree_data = {
            'degree_type': 'BS',
            'degree_name': 'Computer Engineering',
            'school': 'ECE',
            'term': 'Fa2019'
        }
        self.compe_degree = Degree.objects.create(**compe_degree_data)
        self.compe_degree.save()

        test_student_data = {
            'name': 'Jude Lei',
            'password': 'HelloWorld!@#',
            'email': 'jadham@purdue.edu',
            'degree': self.compe_degree,
            'curr_plan': {}
        }
        self.test_student = User.objects.create(**test_student_data)
        self.test_student.save()

    def test_create_user_valid(self):
        test_user_data = {
            'name': 'Jess Zhang',
            'password': 'graphsRox',
            'email': 'jzhang@purdue.edu',
            'degree': self.compe_degree.degree_id,
            'curr_plan': {}
        }
        user_resp = self.client.post(
            reverse('create_get_users'),
            data=test_user_data,
            format='json'
        )

        self.assertEqual(user_resp.status_code, status.HTTP_201_CREATED)
        user_resp = user_resp.json()
        self.assertTrue('user_id' in user_resp)

    def test_create_user_invalid(self):
        test_user_data = {
            'name': 'Jess Zhang',
            'password': 'graphsRox',
            'email': 'jzhang@purdue.edu',
            'curr_plan': {}
        }
        user_resp = self.client.post(
            reverse('create_get_users'),
            data=test_user_data,
            format='json'
        )

        self.assertEqual(user_resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_all_users_update(self):
        update_test_user_data = {
            'name': 'Jezz Zhang',
            'password': 'b293jfsq32',
            'email': 'jzhang@purdue.edu',
            'degree': self.compe_degree,
            'curr_plan': {}
        }
        test_user = User.objects.create(**update_test_user_data)
        test_user.save()

        get_users_resp = self.client.get(
            reverse('create_get_users'),
            format='json'
        )
        get_users_resp = get_users_resp.json()

        self.assertEqual(len(get_users_resp), 2)

    def test_get_user_id_valid(self):
        get_user_resp = self.client.get(
            reverse('detail_user', kwargs={'user_id': self.test_student.user_id}),
            format='json'
        )
        get_user_resp = get_user_resp.json()

        self.assertEqual(self.test_student.user_id, get_user_resp['user_id'])

    def test_get_user_id_invalid(self):
        get_user_resp = self.client.get(
            reverse('detail_user', kwargs={'user_id': 12415134}),
            format='json'
        )

        self.assertEqual(get_user_resp.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_user_id_valid(self):
        new_user_data = {
            'name': 'Jess Zhang',
            'password': 'graphsRox',
            'email': 'jzhang@purdue.edu',
            'degree': self.compe_degree,
            'curr_plan': {}
        }
        new_user = User.objects.create(**new_user_data)

        update_data = {
            'name': 'Jude Adham',
            'password': 'pwned123',
            'email': 'newlegitemail@purdue.edu',
            'degree': self.compe_degree.degree_id,
            'curr_plan': {}
        }

        put_user_resp = self.client.put(
            reverse('detail_user', kwargs={'user_id': new_user.user_id}),
            data=update_data,
            format='json'
        )
        self.assertEqual(put_user_resp.status_code, status.HTTP_200_OK)

        put_user_resp = put_user_resp.json()

        self.assertEqual(put_user_resp['email'], 'newlegitemail@purdue.edu')

    def test_update_user_id_invalid(self):
        new_user_data = {
            'name': 'Jess Zhang',
            'password': 'graphsRox',
            'email': 'jzhang@purdue.edu',
            'degree': self.compe_degree,
            'curr_plan': {}
        }
        new_user = User.objects.create(**new_user_data)

        update_data = {'email': 'newlegitemail@purdue.edu'}

        put_user_resp = self.client.put(
            reverse('detail_user', kwargs={'user_id': new_user.user_id}),
            data=update_data,
            format='json'
        )

        self.assertEqual(put_user_resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_user_id_valid(self):
        new_user_data = {
            'name': 'Jess Zhang',
            'password': 'graphsRox',
            'email': 'jzhang@purdue.edu',
            'degree': self.compe_degree,
            'curr_plan': {}
        }
        new_user = User.objects.create(**new_user_data)
        new_user_user_id = new_user.user_id

        put_user_resp = self.client.delete(
            reverse('detail_user', kwargs={'user_id': new_user.user_id}),
            format='json'
        )

        self.assertEqual(put_user_resp.status_code, status.HTTP_200_OK)
        self.assertFalse(User.objects.filter(user_id=new_user_user_id).exists())

    def test_delete_user_id_invalid(self):
        put_user_resp = self.client.delete(
            reverse('detail_user', kwargs={'user_id': 12313252}),
            format='json'
        )

        self.assertEqual(put_user_resp.status_code, status.HTTP_404_NOT_FOUND)


class DegreeTests(APITestCase):
    def setUp(self):
        compe_degree_data = {
            'degree_type': 'BS',
            'degree_name': 'Computer Engineering',
            'school': 'ECE',
            'term': 'Fa2019'
        }
        self.compe_degree = Degree.objects.create(**compe_degree_data)
        self.compe_degree.save()

        test_student_data = {
            'name': 'Jude Lei',
            'password': 'HelloWorld!@#',
            'email': 'jadham@purdue.edu',
            'degree': self.compe_degree,
            'curr_plan': {}
        }
        self.test_student = User.objects.create(**test_student_data)
        self.test_student.save()

    def test_create_degree_valid(self):
        test_degree_data = {
            'degree_type': 'BA',
            'degree_name': 'English',
            'school': 'ENGL',
            'term': 'Fa2020'
        }
        degree_resp = self.client.post(
            reverse('create_get_degrees'),
            data=test_degree_data,
            format='json'
        )

        self.assertEqual(degree_resp.status_code, status.HTTP_201_CREATED)
        degree_resp = degree_resp.json()
        self.assertTrue('degree_id' in degree_resp)

    def test_create_degree_invalid(self):
        test_degree_data = {
            'degree_type': 'BA',
            'degree_name': 'Computer CRUDgineering',
            'term': 'Sm2095'
        }
        degree_resp = self.client.post(
            reverse('create_get_degrees'),
            data=test_degree_data,
            format='json'
        )

        self.assertEqual(get_user_resp.status_code, status.HTTP_404_NOT_FOUND)

class CourseTests(APITestCase):
    def setUp(self):
        test_course_data = {
            'course_name': 'Electrical Engineering Fundamentals I',
            'course_tag': 'ECE 20001',
            'course_credits': 3,
            'description': 'This course covers fundamental concepts and applications for electrical and computer engineers.',
            'terms': 'Fa2021, Sp2022'
        }
        self.test_course = Course.objects.create(**test_course_data)
        self.test_course.save()

    def test_create_course_valid(self):
        test_course_data = {
            'course_name': 'Electrical Engineering Fundamentals I',
            'course_tag': 'ECE 20001',
            'course_credits': 3,
            'description': 'This course covers fundamental concepts and applications for electrical and computer engineers.',
            'terms': 'Fa2021, Sp2022'
        }
        course_resp = self.client.post(
            reverse('create_get_courses'),
            data=test_course_data,
            format='json'
        )

        self.assertEqual(course_resp.status_code, status.HTTP_201_CREATED)
        course_resp = course_resp.json()
        self.assertTrue('course_id' in course_resp)

    def test_create_course_invalid(self):
        test_course_data = {
            'course_name': 'Electrical Engineering Fundamentals I',
            'course_tag': 'ECE 20001',
            'description': 'This course covers fundamental concepts and applications for electrical and computer engineers.',
            'terms': 'Fa2021, Sp2022'
        }
        course_resp = self.client.post(
            reverse('create_get_courses'),
            data=test_course_data,
            format='json'
        )

        self.assertEqual(course_resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_all_courses_empty(self):
        get_courses_resp = self.client.get(
            reverse('create_get_courses'),
            format='json'
        )
        get_courses_resp = get_courses_resp.json()

        self.assertFalse(get_courses_resp)

    def test_get_all_courses_nonempty(self):
        test_course_data = {
            'course_name': 'Electrical Engineering Fundamentals I',
            'course_tag': 'ECE 20001',
            'course_credits': 3,
            'description': 'This course covers fundamental concepts and applications for electrical and computer engineers.',
            'terms': 'Fa2021, Sp2022'
        }
        test_course = Course.objects.create(**test_course_data)
        test_course.save()

        get_courses_resp = self.client.get(
            reverse('create_get_courses'),
            format='json'
        )
        get_courses_resp = get_courses_resp.json()

        self.assertEqual(len(get_courses_resp), 1)

    def test_get_course_id_valid(self):
        test_course_data = {
            'course_name': 'Electrical Engineering Fundamentals I',
            'course_tag': 'ECE 20001',
            'course_credits': 3,
            'description': 'This course covers fundamental concepts and applications for electrical and computer engineers.',
            'terms': 'Fa2021, Sp2022'
        }
        test_course = Course.objects.create(**test_course_data)
        test_course.save()

        get_course_resp = self.client.get(
            reverse('detail_course', args=[test_course.course_id]),
            format='json'
        )
        get_course_resp = get_course_resp.json()

        self.assertEqual(test_course.course_id, get_course_resp['course_id'])

    def test_get_course_id_invalid(self):
        get_course_resp = self.client.get(
            reverse('detail_course', args=[1]),
            format='json'
        )

        self.assertEqual(get_course_resp.status_code, status.HTTP_404_NOT_FOUND)
