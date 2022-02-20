from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from MakeMyDegree.models import *


class UserDegreeTests(APITestCase):
    def test_create_degree_valid(self):
        test_degree_data = {
            'degree_type': 'BS',
            'degree_name': 'Computer Engineering',
            'school': 'ECE',
            'term': 'Fa2019'
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

        self.assertEqual(degree_resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_valid(self):
        test_degree_data = {
            'degree_type': 'BS',
            'degree_name': 'Computer Engineering',
            'school': 'ECE',
            'term': 'Fa2019'
        }
        degree_resp = self.client.post(
            reverse('create_get_degrees'),
            data=test_degree_data,
            format='json'
        )

        self.assertEqual(degree_resp.status_code, status.HTTP_201_CREATED)
        degree_resp = degree_resp.json()
        self.assertTrue('degree_id' in degree_resp)

        test_user_data = {
            'name': 'Jude Lei',
            'password': 'graphsRox',
            'email': 'jadham@purdue.edu',
            'degree': degree_resp['degree_id'],
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
        test_degree_data = {
            'degree_type': 'BS',
            'degree_name': 'Computer Engineering',
            'school': 'ECE',
            'term': 'Fa2019'
        }
        degree_resp = self.client.post(
            reverse('create_get_degrees'),
            data=test_degree_data,
            format='json'
        )

        self.assertEqual(degree_resp.status_code, status.HTTP_201_CREATED)
        degree_resp = degree_resp.json()
        self.assertTrue('degree_id' in degree_resp)

        test_user_data = {
            'name': 'Jude Lei',
            'password': 'graphsRox',
            'email': 'jadham@purdue.edu',
            'curr_plan': {}
        }
        user_resp = self.client.post(
            reverse('create_get_users'),
            data=test_user_data,
            format='json'
        )

        self.assertEqual(user_resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_all_users_empty(self):
        get_users_resp = self.client.get(
            reverse('create_get_users'),
            format='json'
        )
        get_users_resp = get_users_resp.json()

        self.assertFalse(get_users_resp)

    def test_get_all_users_nonempty(self):
        test_degree_data = {
            'degree_type': 'BS',
            'degree_name': 'Computer Engineering',
            'school': 'ECE',
            'term': 'Fa2019'
        }
        test_degree = Degree.objects.create(**test_degree_data)
        test_degree.save()

        test_user_data = {
            'name': 'Jezz Zhang',
            'password': 'b293jfsq32',
            'email': 'jzhang@purdue.edu',
            'degree': test_degree,
            'curr_plan': {}
        }
        test_user = User.objects.create(**test_user_data)
        test_user.save()

        test_user_data = {
            'name': 'Jude Adham',
            'password': 'gjioe4h4eiog',
            'email': 'jadham@purdue.edu',
            'degree': test_degree,
            'curr_plan': {}
        }
        test_user = User.objects.create(**test_user_data)
        test_user.save()

        get_users_resp = self.client.get(
            reverse('create_get_users'),
            format='json'
        )
        get_users_resp = get_users_resp.json()

        self.assertEqual(len(get_users_resp), 2)

    def test_get_user_id_valid(self):
        test_degree_data = {
            'degree_type': 'BS',
            'degree_name': 'Computer Engineering',
            'school': 'ECE',
            'term': 'Fa2019'
        }
        test_degree = Degree.objects.create(**test_degree_data)
        test_degree.save()

        test_user_data = {
            'name': 'Jezz Zhang',
            'password': 'b293jfsq32',
            'email': 'jzhang@purdue.edu',
            'degree': test_degree,
            'curr_plan': {}
        }
        test_user = User.objects.create(**test_user_data)
        test_user.save()

        get_user_resp = self.client.get(
            reverse('detail_user', args=[test_user.user_id]),
            format='json'
        )
        get_user_resp = get_user_resp.json()

        self.assertEqual(test_user.user_id, get_user_resp['user_id'])

    def test_get_user_id_invalid(self):
        get_user_resp = self.client.get(
            reverse('detail_user', args=[1]),
            format='json'
        )

        self.assertEqual(get_user_resp.status_code, status.HTTP_404_NOT_FOUND)

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

    
    