from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from MakeMyDegree.models import *


class UserDegreeTests(APITestCase):
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
            reverse('detail_user', args=[self.test_student.user_id]),
            format='json'
        )
        get_user_resp = get_user_resp.json()

        self.assertEqual(self.test_student.user_id, get_user_resp['user_id'])

    def test_get_user_id_invalid(self):
        get_user_resp = self.client.get(
            reverse('detail_user', args=[1]),
            format='json'
        )

        self.assertEqual(get_user_resp.status_code, status.HTTP_404_NOT_FOUND)


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

        self.assertEqual(degree_resp.status_code, status.HTTP_400_BAD_REQUEST)
