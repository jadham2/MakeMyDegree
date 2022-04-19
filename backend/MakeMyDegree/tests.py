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

    def test_get_all_users_valid(self):
        new_user_data = {
            'name': 'Jezz Zhang',
            'password': 'b293jfsq32',
            'email': 'jzhang@purdue.edu',
            'degree': self.compe_degree,
            'curr_plan': {}
        }
        test_user = User.objects.create(**new_user_data)
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

        self.assertEqual(put_user_resp['email'], update_data['email'])

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
        new_user_id = new_user.user_id

        delete_user_resp = self.client.delete(
            reverse('detail_user', kwargs={'user_id': new_user.user_id}),
            format='json'
        )

        self.assertEqual(delete_user_resp.status_code, status.HTTP_200_OK)
        self.assertFalse(User.objects.filter(user_id=new_user_id).exists())

    def test_delete_user_id_invalid(self):
        delete_user_resp = self.client.delete(
            reverse('detail_user', kwargs={'user_id': 12313252}),
            format='json'
        )

        self.assertEqual(delete_user_resp.status_code, status.HTTP_404_NOT_FOUND)


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

    def test_get_all_degrees_valid(self):
        update_test_degree_data = {
            'degree_type': 'BA',
            'degree_name': 'English',
            'school': 'ENGL',
            'term': 'Fa2020'
        }
        test_degree = Degree.objects.create(**update_test_degree_data)
        test_degree.save()

        get_degrees_resp = self.client.get(
            reverse('create_get_degrees'),
            format='json'
        )
        get_degrees_json = get_degrees_resp.json()

        self.assertEqual(len(get_degrees_json), 2)

    def test_get_degree_id_valid(self):
        get_degree_resp = self.client.get(
            reverse('detail_degree', kwargs={'degree_id': self.compe_degree.degree_id}),
            format='json'
        )
        get_degree_resp = get_degree_resp.json()

        self.assertEqual(self.compe_degree.degree_id, get_degree_resp['degree_id'])

    def test_get_degree_id_invalid(self):
        get_degree_resp = self.client.get(
            reverse('detail_degree', kwargs={'degree_id': 12415134}),
            format='json'
        )

        self.assertEqual(get_degree_resp.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_degree_id_valid(self):
        new_data = {
            'degree_type': 'BS',
            'degree_name': 'Computer Engineering',
            'school': 'ECE',
            'term': 'Fa2019'
        }
        new_degree = Degree.objects.create(**new_data)

        update_data = {
            'degree_type': 'BA',
            'degree_name': 'English',
            'school': 'ENGL',
            'term': 'Fa2020'
        }

        put_degree_resp = self.client.put(
            reverse('detail_degree', kwargs={'degree_id': new_degree.degree_id}),
            data=update_data,
            format='json'
        )
        self.assertEqual(put_degree_resp.status_code, status.HTTP_200_OK)

        put_degree_resp = put_degree_resp.json()

        self.assertEqual(put_degree_resp['degree_name'], update_data['degree_name'])

    def test_update_degree_id_invalid(self):
        new_data = {
            'degree_type': 'BS',
            'degree_name': 'Computer Engineering',
            'school': 'ECE',
            'term': 'Fa2019'
        }
        new_degree = Degree.objects.create(**new_data)

        update_data = {'degree_type': 'BA'}

        put_degree_resp = self.client.put(
            reverse('detail_degree', kwargs={'degree_id': new_degree.degree_id}),
            data=update_data,
            format='json'
        )

        self.assertEqual(put_degree_resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_degree_id_valid(self):
        new_data = {
            'degree_type': 'BS',
            'degree_name': 'Computer Engineering',
            'school': 'ECE',
            'term': 'Fa2019'
        }
        new_degree = Degree.objects.create(**new_data)
        new_degree_id = new_degree.degree_id

        delete_degree_resp = self.client.delete(
            reverse('detail_degree', kwargs={'degree_id': new_degree.degree_id}),
            format='json'
        )

        self.assertEqual(delete_degree_resp.status_code, status.HTTP_200_OK)
        self.assertFalse(Degree.objects.filter(degree_id=new_degree_id).exists())

    def test_delete_degree_id_invalid(self):
        delete_degree_resp = self.client.delete(
            reverse('detail_degree', kwargs={'degree_id': 12313252}),
            format='json'
        )

        self.assertEqual(delete_degree_resp.status_code, status.HTTP_404_NOT_FOUND)

    def test_fetch_degree_tags_id_valid(self):
        cs_degree_data = {
            'degree_type': 'BS',
            'degree_name': 'Computer Science',
            'school': 'CS',
            'term': 'Fa2020'
        }
        cs_degree = Degree.objects.create(**cs_degree_data)
        cs_degree.save()

        test_tag_data_1 = {
            'degree': cs_degree,
            'name': 'General Education 1',
            'rule': '>= 17'
        }
        test_tag_data_2 = {
            'degree': cs_degree,
            'name': 'General Education 2',
            'rule': '>= 17'
        }
        test_tag_1 = Tag.objects.create(**test_tag_data_1)
        test_tag_2 = Tag.objects.create(**test_tag_data_2)
        test_tag_1.save()
        test_tag_2.save()

        degree_tags_resp = self.client.get(
            reverse('fetch_degree_tags', kwargs={'degree_id': cs_degree.degree_id}),
            format='json'
        )

        self.assertEqual(degree_tags_resp.status_code, status.HTTP_200_OK)
        self.assertTrue(test_tag_data_1['name'] in str(degree_tags_resp.content))
        self.assertTrue(test_tag_data_2['name'] in str(degree_tags_resp.content))

        cs_degree.delete()

    def test_fetch_degree_tags_id_invalid(self):
        cs_degree_data = {
            'degree_type': 'BS',
            'degree_name': 'Computer Science',
            'school': 'CS',
            'term': 'Fa2020'
        }
        cs_degree = Degree.objects.create(**cs_degree_data)
        cs_degree.save()

        test_tag_data_1 = {
            'degree': cs_degree,
            'name': 'General Education 1',
            'rule': '>= 17'
        }
        test_tag_data_2 = {
            'degree': cs_degree,
            'name': 'General Education 2',
            'rule': '>= 17'
        }
        test_tag_1 = Tag.objects.create(**test_tag_data_1)
        test_tag_2 = Tag.objects.create(**test_tag_data_2)
        test_tag_1.save()
        test_tag_2.save()

        fake_degree_data = {
            'degree_type': 'BS',
            'degree_name': 'Not a real degree',
            'school': 'Business',
            'term': 'Fa2020'
        }
        fake_degree = Degree.objects.create(**fake_degree_data)
        degree_tags_resp = self.client.get(
            reverse('fetch_degree_tags', kwargs={'degree_id': fake_degree.degree_id}),
            format='json'
        )
        self.assertEqual(degree_tags_resp.status_code, status.HTTP_404_NOT_FOUND)

        cs_degree.delete()


class CourseTests(APITestCase):
    def setUp(self):
        test_course_data = {
            'course_name': 'Electrical Engineering Fundamentals I',
            'course_tag': 'ECE 20001',
            'course_credits': 3,
            'description': 'This course covers fundamental concepts and applications for electrical and computer engineers.',
            'terms': ['Fa2021']
        }
        self.test_course = Course.objects.create(**test_course_data)
        self.test_course.save()

    def test_create_course_valid(self):
        test_course_data = {
            'course_name': 'Electrical Engineering Fundamentals I',
            'course_tag': 'ECE 20001',
            'course_credits': 3,
            'description': 'This course covers fundamental concepts and applications for electrical and computer engineers.',
            'terms': ['Fa2021']
        }
        course_resp = self.client.post(
            reverse('create_get_courses'),
            data=test_course_data,
            format='json'
        )

        self.assertEqual(course_resp.status_code, status.HTTP_201_CREATED)
        course_resp = course_resp.json()
        self.assertTrue('course_id' in course_resp)

    def test_create_course_empty_term(self):
        test_course_data = {
            'course_name': 'Electrical Engineering Fundamentals I',
            'course_tag': 'ECE 20001',
            'course_credits': 3,
            'description': 'This course covers fundamental concepts and applications for electrical and computer engineers.',
            'terms': []
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
            'terms': ['Fa2021']
        }
        course_resp = self.client.post(
            reverse('create_get_courses'),
            data=test_course_data,
            format='json'
        )

        self.assertEqual(course_resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_all_courses_valid(self):
        update_test_course_data = {
            'course_name': 'Electrical Engineering Fundamentals I',
            'course_tag': 'ECE 20001',
            'course_credits': 3,
            'description': 'This course covers fundamental concepts and applications for electrical and computer engineers.',
            'terms': ['Fa2021']
        }

        test_course = Course.objects.create(**update_test_course_data)
        test_course.save()

        get_courses_resp = self.client.get(
            reverse('create_get_courses'),
            format='json'
        )
        get_courses_resp = get_courses_resp.json()

        self.assertEqual(len(get_courses_resp), 2)

    def test_get_course_id_valid(self):
        get_course_resp = self.client.get(
            reverse('detail_course', kwargs={'course_id': self.test_course.course_id}),
            format='json'
        )
        get_course_resp = get_course_resp.json()

        self.assertEqual(self.test_course.course_id, get_course_resp['course_id'])

    def test_get_course_id_invalid(self):
        get_course_resp = self.client.get(
            reverse('detail_course', kwargs={'course_id': 1231232123}),
            format='json'
        )

        self.assertEqual(get_course_resp.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_course_id_valid(self):
        new_course_data = {
            'course_name': 'Electrical Engineering Fundamentals II',
            'course_tag': 'ECE 20002',
            'course_credits': 3,
            'description': 'This course covers fundamental concepts and applications for electrical and computer engineers.',
            'terms': ['Fa2021']
        }
        new_course = Course.objects.create(**new_course_data)

        update_data = {
            'course_name': 'Electrical Engineering Fundamentals I Lab',
            'course_tag': 'ECE 20007',
            'course_credits': 1,
            'description': 'This course covers fundamental concepts and applications for electrical and computer engineers.',
            'terms': ['Fa2021']
        }

        put_course_resp = self.client.put(
            reverse('detail_course', kwargs={'course_id': new_course.course_id}),
            data=update_data,
            format='json'
        )
        self.assertEqual(put_course_resp.status_code, status.HTTP_200_OK)

        put_course_resp = put_course_resp.json()

        self.assertEqual(put_course_resp['course_tag'], update_data['course_tag'])

    def test_update_course_id_invalid(self):
        new_course_data = {
            'course_name': 'Electrical Engineering Fundamentals II',
            'course_tag': 'ECE 20002',
            'course_credits': 3,
            'description': 'This course covers fundamental concepts and applications for electrical and computer engineers.',
            'terms': ['Fa2021']
        }
        new_course = Course.objects.create(**new_course_data)

        update_data = {'course_name': 'Not an ECE class'}

        put_course_resp = self.client.put(
            reverse('detail_course', kwargs={'course_id': new_course.course_id}),
            data=update_data,
            format='json'
        )

        self.assertEqual(put_course_resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_course_id_valid(self):
        new_course_data = {
            'course_name': 'Electrical Engineering Fundamentals II',
            'course_tag': 'ECE 20002',
            'course_credits': 3,
            'description': 'This course covers fundamental concepts and applications for electrical and computer engineers.',
            'terms': ['Fa2021']
        }
        new_course = Course.objects.create(**new_course_data)
        new_course_id = new_course.course_id

        delete_course_resp = self.client.delete(
            reverse('detail_course', kwargs={'course_id': new_course.course_id}),
            format='json'
        )

        self.assertEqual(delete_course_resp.status_code, status.HTTP_200_OK)
        self.assertFalse(Course.objects.filter(course_id=new_course_id).exists())

    def test_delete_course_id_invalid(self):
        delete_course_resp = self.client.delete(
            reverse('detail_course', kwargs={'course_id': 123132}),
            format='json'
        )

        self.assertEqual(delete_course_resp.status_code, status.HTTP_404_NOT_FOUND)


class TagTests(APITestCase):
    def setUp(self):
        compe_degree_data = {
            'degree_type': 'BS',
            'degree_name': 'Computer Engineering',
            'school': 'ECE',
            'term': 'Fa2019'
        }
        self.compe_degree = Degree.objects.create(**compe_degree_data)
        self.compe_degree.save()

    def test_create_tag_valid(self):
        test_tag_data = {
            'degree': self.compe_degree.degree_id,
            'name': 'General Education',
            'rule': '>= 17'
        }

        tag_resp = self.client.post(
            reverse('create_get_tags'),
            data=test_tag_data,
            format='json'
        )

        self.assertEqual(tag_resp.status_code, status.HTTP_201_CREATED)

        tag_resp = tag_resp.json()

        self.assertEqual(tag_resp['name'], test_tag_data['name'])
        self.assertEqual(tag_resp['degree'], self.compe_degree.degree_id)

    def test_create_tag_invalid_degree(self):
        test_tag_data = {
            'degree': 25325234,
            'name': 'General Education',
            'rule': '>= 17'
        }

        tag_resp = self.client.post(
            reverse('create_get_tags'),
            data=test_tag_data,
            format='json'
        )

        self.assertEqual(tag_resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_all_tags_valid(self):
        test_tag_data = {
            'degree': self.compe_degree,
            'name': 'General Education',
            'rule': '>= 17'
        }
        test_tag = Tag.objects.create(**test_tag_data)
        test_tag.save()

        test_tag_data = {
            'degree': self.compe_degree,
            'name': 'Selectives',
            'rule': '>= 16'
        }

        test_tag = Tag.objects.create(**test_tag_data)
        test_tag.save()

        get_tags_resp = self.client.get(
            reverse('create_get_tags'),
            format='json'
        )

        self.assertEqual(get_tags_resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(get_tags_resp.json()), 2)

    def test_get_all_tags_empty(self):
        get_tags_resp = self.client.get(
            reverse('create_get_tags'),
            format='json'
        )

        self.assertEqual(get_tags_resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(get_tags_resp.json()), 0)

    def test_get_tag_id_valid(self):
        test_tag_data = {
            'degree': self.compe_degree,
            'name': 'General Education',
            'rule': '>= 17'
        }
        test_tag = Tag.objects.create(**test_tag_data)
        test_tag.save()

        get_tag_resp = self.client.get(
            reverse('detail_tag', kwargs={'tag_id': test_tag.tag_id}),
            format='json'
        )

        self.assertEqual(get_tag_resp.status_code, status.HTTP_200_OK)

        get_tag_resp = get_tag_resp.json()

        self.assertEqual(get_tag_resp['name'], test_tag_data['name'])
        self.assertEqual(get_tag_resp['degree'], self.compe_degree.degree_id)

    def test_get_tag_id_invalid(self):
        get_tag_resp = self.client.get(
            reverse('detail_tag', kwargs={'tag_id': 123132}),
            format='json'
        )

        self.assertEqual(get_tag_resp.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_tag_id_valid(self):
        test_tag_data = {
            'degree': self.compe_degree,
            'name': 'General Education',
            'rule': '>= 17'
        }
        test_tag = Tag.objects.create(**test_tag_data)
        test_tag.save()

        update_data = {
            'degree': self.compe_degree.degree_id,
            'name': 'Selectives',
            'rule': '>= 16'
        }

        put_tag_resp = self.client.put(
            reverse('detail_tag', kwargs={'tag_id': test_tag.tag_id}),
            data=update_data,
            format='json'
        )

        self.assertEqual(put_tag_resp.status_code, status.HTTP_200_OK)

        put_tag_resp = put_tag_resp.json()

        self.assertEqual(put_tag_resp['name'], update_data['name'])
        self.assertEqual(put_tag_resp['degree'], self.compe_degree.degree_id)

    def test_update_tag_id_invalid(self):
        update_data = {'name': 'Selectives'}

        put_tag_resp = self.client.put(
            reverse('detail_tag', kwargs={'tag_id': 123132}),
            data=update_data,
            format='json'
        )

        self.assertEqual(put_tag_resp.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_tag_id_valid(self):
        test_tag_data = {
            'degree': self.compe_degree,
            'name': 'General Education',
            'rule': '>= 17'
        }
        test_tag = Tag.objects.create(**test_tag_data)
        test_tag.save()

        delete_tag_resp = self.client.delete(
            reverse('detail_tag', kwargs={'tag_id': test_tag.tag_id}),
            format='json'
        )

        self.assertEqual(delete_tag_resp.status_code, status.HTTP_200_OK)

    def test_delete_tag_id_invalid(self):
        delete_tag_resp = self.client.delete(
            reverse('detail_tag', kwargs={'tag_id': 123132}),
            format='json'
        )

        self.assertEqual(delete_tag_resp.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_degree_existing_tag(self):
        cs_degree_data = {
            'degree_type': 'BS',
            'degree_name': 'Computer Science',
            'school': 'CS',
            'term': 'Fa2020'
        }
        cs_degree = Degree.objects.create(**cs_degree_data)
        cs_degree.save()

        test_tag_data = {
            'degree': cs_degree,
            'name': 'General Education',
            'rule': '>= 17'
        }
        test_tag = Tag.objects.create(**test_tag_data)
        test_tag.save()

        cs_degree.delete()

        # Ensure that once we delete a degree, all tag objects associated with it are also deleted.
        # This is because the tag_id is a foreign key to the degree table and it's on_delete is set to CASCADE.
        self.assertFalse(Tag.objects.filter(tag_id=test_tag.tag_id).exists())


class CourseTagTests(APITestCase):
    def setUp(self):
        self.compe_degree = Degree.objects.create(
            degree_type='BS',
            degree_name='Computer Engineering',
            school='ECE',
            term='Fa2019'
        )
        self.compe_degree.save()

        self.compe_course = Course.objects.create(
            course_name='Linear Circuit Analysis I',
            course_tag='ECE 20001',
            course_credits=3,
            description='Second Year Circuits Course.',
            terms=['Fa2019', 'Fa2020', 'Fa2021']
        )
        self.compe_course.save()

        self.compe_tag = Tag.objects.create(
            degree=self.compe_degree,
            name='General Education',
            rule='>= 17'
        )
        self.compe_tag.save()

    def test_create_course_tag_valid(self):
        test_course_tag_data = {
            'course_id': self.compe_course.course_id,
            'tag_id': self.compe_tag.tag_id
        }

        post_course_tag_resp = self.client.post(
            reverse('create_get_course_tags'),
            data=test_course_tag_data,
            format='json'
        )

        self.assertEqual(post_course_tag_resp.status_code, status.HTTP_201_CREATED)

        post_course_tag_resp = post_course_tag_resp.json()

        self.assertEqual(post_course_tag_resp['course_id'], self.compe_course.course_id)
        self.assertEqual(post_course_tag_resp['tag_id'], self.compe_tag.tag_id)

    def test_create_course_tag_invalid(self):
        test_course_tag_data = {
            'course_id': self.compe_course.course_id,
            'tag_id': 123132
        }

        post_course_tag_resp = self.client.post(
            reverse('create_get_course_tags'),
            data=test_course_tag_data,
            format='json'
        )

        self.assertEqual(post_course_tag_resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_all_course_tags_valid(self):
        test_course_tag_data = {
            'course_id': self.compe_course,
            'tag_id': self.compe_tag
        }

        CourseTag.objects.create(**test_course_tag_data)

        get_course_tags_resp = self.client.get(
            reverse('create_get_course_tags'),
            format='json'
        )

        self.assertEqual(get_course_tags_resp.status_code, status.HTTP_200_OK)

        get_course_tags_resp = get_course_tags_resp.json()

        self.assertEqual(len(get_course_tags_resp), 1)

    def test_get_all_course_tags_empty(self):
        get_course_tags_resp = self.client.get(
            reverse('create_get_course_tags'),
            format='json'
        )

        self.assertEqual(get_course_tags_resp.status_code, status.HTTP_200_OK)

        get_course_tags_resp = get_course_tags_resp.json()

        self.assertEqual(len(get_course_tags_resp), 0)

    def test_get_course_tag_id_valid(self):
        test_course_tag_data = {
            'course_id': self.compe_course,
            'tag_id': self.compe_tag
        }

        course_tag = CourseTag.objects.create(**test_course_tag_data)

        get_course_tag_resp = self.client.get(
            reverse('detail_course_tag', kwargs={'course_tag_id': course_tag.course_tag_id}),
            format='json'
        )

        self.assertEqual(get_course_tag_resp.status_code, status.HTTP_200_OK)

        get_course_tag_resp = get_course_tag_resp.json()

        self.assertEqual(get_course_tag_resp['course_id'], self.compe_course.course_id)
        self.assertEqual(get_course_tag_resp['tag_id'], self.compe_tag.tag_id)

    def test_get_course_tag_id_invalid(self):
        get_course_tag_resp = self.client.get(
            reverse('detail_course_tag', kwargs={'course_tag_id': 123132}),
            format='json'
        )

        self.assertEqual(get_course_tag_resp.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_course_tag_id_valid(self):
        test_course_tag_data = {
            'course_id': self.compe_course,
            'tag_id': self.compe_tag
        }

        course_tag = CourseTag.objects.create(**test_course_tag_data)

        update_course_tag_resp = self.client.put(
            reverse('detail_course_tag', kwargs={'course_tag_id': course_tag.course_tag_id}),
            data={'course_id': self.compe_course.course_id, 'tag_id': self.compe_tag.tag_id},
            format='json'
        )

        self.assertEqual(update_course_tag_resp.status_code, status.HTTP_200_OK)

        update_course_tag_resp = update_course_tag_resp.json()

        self.assertEqual(update_course_tag_resp['course_id'], self.compe_course.course_id)
        self.assertEqual(update_course_tag_resp['tag_id'], self.compe_tag.tag_id)

    def test_update_course_tag_id_invalid(self):
        update_course_tag_resp = self.client.put(
            reverse('detail_course_tag', kwargs={'course_tag_id': 123132}),
            data={'course_id': self.compe_course.course_id, 'tag_id': self.compe_tag.tag_id},
            format='json'
        )

        self.assertEqual(update_course_tag_resp.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_course_tag_id_valid(self):
        test_course_tag_data = {
            'course_id': self.compe_course,
            'tag_id': self.compe_tag
        }

        course_tag = CourseTag.objects.create(**test_course_tag_data)

        delete_course_tag_resp = self.client.delete(
            reverse('detail_course_tag', kwargs={'course_tag_id': course_tag.course_tag_id}),
            format='json'
        )

        self.assertEqual(delete_course_tag_resp.status_code, status.HTTP_200_OK)

    def test_delete_course_tag_id_invalid(self):
        delete_course_tag_resp = self.client.delete(
            reverse('detail_course_tag', kwargs={'course_tag_id': 123132}),
            format='json'
        )

        self.assertEqual(delete_course_tag_resp.status_code, status.HTTP_404_NOT_FOUND)


class RequisiteTests(APITestCase):
    def setUp(self):
        self.compe_course1 = Course.objects.create(
            course_name='Linear Circuit Analysis I',
            course_tag='ECE 20001',
            course_credits=3,
            description='Second Year Circuits Course.',
            terms=['Fa2019', 'Fa2020', 'Fa2021']
        )
        self.compe_course1.save()

        self.compe_course2 = Course.objects.create(
            course_name='Linear Circuit Analysis II',
            course_tag='ECE 20002',
            course_credits=3,
            description='Second Year Circuits Course.',
            terms=['Sp2020', 'Sp2021', 'Sp2022']
        )
        self.compe_course2.save()

    def test_create_requisite_valid(self):
        test_requisite_data = {
            'course_id': self.compe_course2.course_id,
            'course_requisite': self.compe_course1.course_id,
            'requisite_type': 'Pre'
        }

        requisite = self.client.post(
            reverse('create_get_requisites'),
            data=test_requisite_data,
            format='json'
        )

        self.assertEqual(requisite.status_code, status.HTTP_201_CREATED)

        requisite = requisite.json()

        self.assertEqual(requisite['course_requisite'], self.compe_course1.course_id)
        self.assertEqual(requisite['course_id'], self.compe_course2.course_id)

    def test_create_requisite_invalid(self):
        test_requisite_data = {
            'course_id': 1231312,
            'course_requisite': self.compe_course1.course_id,
            'requisite_type': 'Pre'
        }

        requisite = self.client.post(
            reverse('create_get_requisites'),
            data=test_requisite_data,
            format='json'
        )

        self.assertEqual(requisite.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_requisite_id_valid(self):
        test_requisite_data = {
            'course_id': self.compe_course2.course_id,
            'course_requisite': self.compe_course1.course_id,
            'requisite_type': 'Pre'
        }

        requisite = self.client.post(
            reverse('create_get_requisites'),
            data=test_requisite_data,
            format='json'
        )

        self.assertEqual(requisite.status_code, status.HTTP_201_CREATED)

        requisite = requisite.json()

        get_requisite_resp = self.client.get(
            reverse('detail_requisite', kwargs={'requisite_id': requisite['requisite_id']}),
            format='json'
        )

        self.assertEqual(get_requisite_resp.status_code, status.HTTP_200_OK)

        get_requisite_resp = get_requisite_resp.json()

        self.assertEqual(get_requisite_resp['course_id'], self.compe_course2.course_id)
        self.assertEqual(get_requisite_resp['course_requisite'], self.compe_course1.course_id)

    def test_get_requisite_id_invalid(self):
        get_requisite_resp = self.client.get(
            reverse('detail_requisite', kwargs={'requisite_id': 123132}),
            format='json'
        )

        self.assertEqual(get_requisite_resp.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_requisite_id_valid(self):
        test_requisite_data = {
            'course_id': self.compe_course2.course_id,
            'course_requisite': self.compe_course1.course_id,
            'requisite_type': 'Pre'
        }

        requisite = self.client.post(
            reverse('create_get_requisites'),
            data=test_requisite_data,
            format='json'
        )

        self.assertEqual(requisite.status_code, status.HTTP_201_CREATED)

        requisite = requisite.json()

        update_requisite_resp = self.client.put(
            reverse('detail_requisite', kwargs={'requisite_id': requisite['requisite_id']}),
            data={'course_id': self.compe_course1.course_id, 'course_requisite': self.compe_course2.course_id, 'requisite_type': 'Pre'},
            format='json'
        )

        self.assertEqual(update_requisite_resp.status_code, status.HTTP_200_OK)

        update_requisite_resp = update_requisite_resp.json()

        self.assertEqual(update_requisite_resp['course_id'], self.compe_course1.course_id)
        self.assertEqual(update_requisite_resp['course_requisite'], self.compe_course2.course_id)

    def test_update_requisite_id_invalid(self):
        update_requisite_resp = self.client.put(
            reverse('detail_requisite', kwargs={'requisite_id': 123132}),
            data={'course_id': self.compe_course1.course_id, 'course_requisite': self.compe_course2.course_id, 'requisite_type': 'Pre'},
            format='json'
        )

        self.assertEqual(update_requisite_resp.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_requisite_id_valid(self):
        test_requisite_data = {
            'course_id': self.compe_course2.course_id,
            'course_requisite': self.compe_course1.course_id,
            'requisite_type': 'Pre'
        }

        requisite = self.client.post(
            reverse('create_get_requisites'),
            data=test_requisite_data,
            format='json'
        )

        self.assertEqual(requisite.status_code, status.HTTP_201_CREATED)

        requisite = requisite.json()

        delete_requisite_resp = self.client.delete(
            reverse('detail_requisite', kwargs={'requisite_id': requisite['requisite_id']}),
            format='json'
        )

        self.assertEqual(delete_requisite_resp.status_code, status.HTTP_200_OK)

    def test_delete_requisite_id_invalid(self):
        delete_requisite_resp = self.client.delete(
            reverse('detail_requisite', kwargs={'requisite_id': 123132}),
            format='json'
        )

        self.assertEqual(delete_requisite_resp.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_requisite_foreign_key(self):

        cs_course_data = {
            'course_name': 'Data Structures',
            'course_tag': 'ECE 20001',
            'course_credits': 3,
            'description': 'Second Year Circuits Course.',
            'terms': ['Fa2019', 'Fa2020', 'Fa2021']
        }

        cs_course = Course.objects.create(**cs_course_data)
        cs_course.save()

        test_requisite_data = {
            'course_id': cs_course,
            'course_requisite': self.compe_course1,
            'requisite_type': 'Pre'
        }

        requisite = Requisite.objects.create(**test_requisite_data)
        requisite.save()

        cs_course.delete()

        self.assertFalse(Requisite.objects.filter(requisite_id=requisite.requisite_id).exists())


class UpdateTests(APITestCase):
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
            'curr_plan': {'Fa2019': [], 'Sp2020': [], 'Su2020': [], 'Fa2020': [], 'Sp2021': [], 'Su2021': []}
        }
        self.test_student = User.objects.create(**test_student_data)
        self.test_student.save()

        test_tag_1 = {
            'degree': self.compe_degree,
            'name': 'Core Courses',
            'rule': '>= 14'
        }
        self.test_tag_1 = Tag.objects.create(**test_tag_1)
        self.test_tag_1.save()

        test_tag_2 = {
            'degree': self.compe_degree,
            'name': 'Selectives',
            'rule': '<= 8'
        }
        self.test_tag_2 = Tag.objects.create(**test_tag_2)
        self.test_tag_2.save()

        circuits_1_course = {
            'course_name': 'Linear Circuit Analysis',
            'course_tag': 'ECE 20001',
            'course_credits': 3,
            'description': 'First Year Circuits Course.',
            'terms': ['Fa2019', 'Fa2020', 'Fa2021']
        }
        self.circuits_1_course = Course.objects.create(**circuits_1_course)
        self.circuits_1_course.save()

        ai_course = {
            'course_name': 'Artificial Intelligence',
            'course_tag': 'ECE 57000',
            'course_credits': 3,
            'description': 'Graduate AI course.',
            'terms': ['Sp2020', 'Sp2021']
        }
        self.ai_course = Course.objects.create(**ai_course)
        self.ai_course.save()

        data_structures_course = {
            'course_name': 'Data Structures',
            'course_tag': 'ECE 36800',
            'course_credits': 3,
            'description': 'Data Structures and Algorithms.',
            'terms': ['Fa2019', 'Sp2020', 'Su2020', 'Fa2020', 'Sp2021', 'Su2021']
        }
        self.data_structures_course = Course.objects.create(**data_structures_course)
        self.data_structures_course.save()

        dig_systems_course = {
            'course_name': 'Digital Systems Design',
            'course_tag': 'ECE 27000',
            'course_credits': 4,
            'description': 'Digital Systems Design.',
            'terms': ['Fa2019', 'Sp2020', 'Su2020', 'Fa2020', 'Sp2021', 'Su2021']
        }
        self.dig_systems_course = Course.objects.create(**dig_systems_course)
        self.dig_systems_course.save()

        os_course = {
            'course_name': 'Operating Systems',
            'course_tag': 'ECE 46900',
            'course_credits': 4,
            'description': 'Operating Systems.',
            'terms': ['Fa2019', 'Sp2020', 'Su2020', 'Fa2020', 'Sp2021', 'Su2021']
        }
        self.os_course = Course.objects.create(**os_course)
        self.os_course.save()

        microprocessor_course = {
            'course_name': 'Microprocessor Systems & Interfacing',
            'course_tag': 'ECE 36200',
            'course_credits': 4,
            'description': 'Microprocessor Systems & Interfacing.',
            'terms': ['Fa2019', 'Sp2020', 'Fa2020', 'Sp2021']
        }
        self.microprocessor_course = Course.objects.create(**microprocessor_course)
        self.microprocessor_course.save()

        signals_course = {
            'course_name': 'Signals and Systems',
            'course_tag': 'ECE 30100',
            'course_credits': 3,
            'description': 'Signals and Systems.',
            'terms': ['Fa2019', 'Sp2020', 'Su2020', 'Fa2020', 'Sp2021', 'Su2021']
        }
        self.signals_course = Course.objects.create(**signals_course)
        self.signals_course.save()

        course_tag_1 = {
            'course_id': self.circuits_1_course,
            'tag_id': self.test_tag_1
        }
        self.course_tag_1 = CourseTag.objects.create(**course_tag_1)
        self.course_tag_1.save()

        course_tag_2 = {
            'course_id': self.ai_course,
            'tag_id': self.test_tag_2
        }
        self.course_tag_2 = CourseTag.objects.create(**course_tag_2)
        self.course_tag_2.save()

        course_tag_3 = {
            'course_id': self.data_structures_course,
            'tag_id': self.test_tag_1
        }
        self.course_tag_3 = CourseTag.objects.create(**course_tag_3)
        self.course_tag_3.save()

        course_tag_4 = {
            'course_id': self.dig_systems_course,
            'tag_id': self.test_tag_1
        }
        self.course_tag_4 = CourseTag.objects.create(**course_tag_4)
        self.course_tag_4.save()

        course_tag_5 = {
            'course_id': self.os_course,
            'tag_id': self.test_tag_2
        }
        self.course_tag_5 = CourseTag.objects.create(**course_tag_5)
        self.course_tag_5.save()

        course_tag_6 = {
            'course_id': self.microprocessor_course,
            'tag_id': self.test_tag_1
        }
        self.course_tag_6 = CourseTag.objects.create(**course_tag_6)
        self.course_tag_6.save()

        course_tag_7 = {
            'course_id': self.signals_course,
            'tag_id': self.test_tag_1
        }
        self.course_tag_7 = CourseTag.objects.create(**course_tag_7)
        self.course_tag_7.save()

        requisite_1 = {
            'course_id': self.ai_course,
            'course_requisite': self.data_structures_course,
            'requisite_type': 'pre'
        }
        self.requisite_1 = Requisite.objects.create(**requisite_1)
        self.requisite_1.save()

        requisite_2 = {
            'course_id': self.os_course,
            'course_requisite': self.data_structures_course,
            'requisite_type': 'pre'
        }
        self.requisite_2 = Requisite.objects.create(**requisite_2)
        self.requisite_2.save()

        requisite_3 = {
            'course_id': self.microprocessor_course,
            'course_requisite': self.dig_systems_course,
            'requisite_type': 'pre'
        }
        self.requisite_3 = Requisite.objects.create(**requisite_3)
        self.requisite_3.save()

        requisite_4 = {
            'course_id': self.signals_course,
            'course_requisite': self.circuits_1_course,
            'requisite_type': 'pre'
        }
        self.requisite_4 = Requisite.objects.create(**requisite_4)
        self.requisite_4.save()

    def test_create_empty_plan(self):
        plan_data = {}

        response = self.client.put(
            reverse('update_plan', kwargs={'user_id': self.test_student.user_id}),
            data=plan_data
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'degree': {str(self.test_tag_1.tag_id): -int(self.test_tag_1.rule.split()[1])}, 'requisites': {}})

    def test_valid_plan(self):
        plan_data = {
            'Fa2019': [self.circuits_1_course.course_id, self.data_structures_course.course_id],
            'Sp2020': [self.ai_course.course_id],
            'Su2020': [self.dig_systems_course.course_id, self.os_course.course_id],
            'Fa2020': [self.microprocessor_course.course_id, self.signals_course.course_id]
        }

        response = self.client.put(
            reverse('update_plan', kwargs={'user_id': self.test_student.user_id}),
            data=plan_data
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'degree': {}, 'requisites': {}})

    def test_missing_core_classes(self):
        plan_data = {
            'Fa2019': [self.circuits_1_course.course_id, self.data_structures_course.course_id],
            'Sp2020': [self.ai_course.course_id],
            'Su2020': [self.dig_systems_course.course_id, self.os_course.course_id],
            'Fa2020': []
        }

        response = self.client.put(
            reverse('update_plan', kwargs={'user_id': self.test_student.user_id}),
            data=plan_data
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'degree': {str(self.test_tag_1.tag_id): -4}, 'requisites': {}})

    def test_overflow_selectives(self):
        new_selective = {
            'course_name': 'Intro to Computer Security',
            'course_tag': 'ECE 40400',
            'course_credits': 3,
            'description': 'Intro to Computer Security.',
            'terms': ['Fa2019', 'Sp2020', 'Su2020', 'Fa2020']
        }
        new_selective = Course.objects.create(**new_selective)
        new_selective.save()

        selective_course_tag = {
            'course_id': new_selective,
            'tag_id': self.test_tag_2
        }
        selective_course_tag = CourseTag.objects.create(**selective_course_tag)
        selective_course_tag.save()

        plan_data = {
            'Fa2019': [self.circuits_1_course.course_id, self.data_structures_course.course_id],
            'Sp2020': [self.ai_course.course_id],
            'Su2020': [self.dig_systems_course.course_id, self.os_course.course_id],
            'Fa2020': [self.microprocessor_course.course_id, self.signals_course.course_id, new_selective.course_id]
        }
        response = self.client.put(
            reverse('update_plan', kwargs={'user_id': self.test_student.user_id}),
            data=plan_data
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'degree': {str(self.test_tag_2.tag_id): 2}, 'requisites': {}})

    def test_missing_prereqs(self):
        plan_data = {
            'Fa2019': [self.circuits_1_course.course_id],
            'Sp2020': [self.ai_course.course_id],
            'Su2020': [self.dig_systems_course.course_id, self.os_course.course_id],
            'Fa2020': [self.microprocessor_course.course_id, self.signals_course.course_id]
        }

        response = self.client.put(
            reverse('update_plan', kwargs={'user_id': self.test_student.user_id}),
            data=plan_data
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                'degree': {},
                'requisites': {
                    str(self.ai_course.course_id): {
                        'pre': [self.data_structures_course.course_id],
                    },
                    str(self.os_course.course_id): {
                        'pre': [self.data_structures_course.course_id]
                    }
                }
            }
        )

    def test_missing_corequisites(self):
        networking_course = {
            'course_name': 'Computer Networking',
            'course_tag': 'ECE 54700',
            'course_credits': 3,
            'description': 'Computer Networking.',
            'terms': ['Fa2019', 'Sp2020', 'Su2020', 'Fa2020']
        }
        networking_course = Course.objects.create(**networking_course)
        networking_course.save()

        test_coreq = {
            'course_id': networking_course,
            'course_requisite': self.signals_course,
            'requisite_type': 'co'
        }
        test_coreq = Requisite.objects.create(**test_coreq)
        test_coreq.save()

        plan_data = {
            'Fa2019': [self.circuits_1_course.course_id, self.data_structures_course.course_id],
            'Sp2020': [self.ai_course.course_id],
            'Su2020': [self.dig_systems_course.course_id, self.os_course.course_id],
            'Fa2020': [self.microprocessor_course.course_id, networking_course.course_id]
        }

        response = self.client.put(
            reverse('update_plan', kwargs={'user_id': self.test_student.user_id}),
            data=plan_data
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                'degree': {},
                'requisites': {
                    str(networking_course.course_id): {
                        'co': [self.signals_course.course_id]
                    }
                }
            }
        )

    def test_missing_pre_and_co_requisites(self):
        networking_course = {
            'course_name': 'Computer Networking',
            'course_tag': 'ECE 54700',
            'course_credits': 3,
            'description': 'Computer Networking.',
            'terms': ['Fa2019', 'Sp2020', 'Su2020', 'Fa2020']
        }
        networking_course = Course.objects.create(**networking_course)
        networking_course.save()

        test_coreq = {
            'course_id': networking_course,
            'course_requisite': self.signals_course,
            'requisite_type': 'co'
        }
        test_coreq = Requisite.objects.create(**test_coreq)
        test_coreq.save()

        plan_data = {
            'Fa2019': [self.circuits_1_course.course_id],
            'Sp2020': [self.ai_course.course_id],
            'Su2020': [self.dig_systems_course.course_id, self.os_course.course_id],
            'Fa2020': [self.microprocessor_course.course_id, networking_course.course_id, self.data_structures_course.course_id]
        }

        response = self.client.put(
            reverse('update_plan', kwargs={'user_id': self.test_student.user_id}),
            data=plan_data
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                'degree': {},
                'requisites': {
                    str(self.ai_course.course_id): {
                        'pre': [self.data_structures_course.course_id],
                    },
                    str(self.os_course.course_id): {
                        'pre': [self.data_structures_course.course_id]
                    },
                    str(networking_course.course_id): {
                        'co': [self.signals_course.course_id]
                    }
                }
            }
        )

    def test_all_audit_requirements(self):
        networking_course = {
            'course_name': 'Computer Networking',
            'course_tag': 'ECE 54700',
            'course_credits': 3,
            'description': 'Computer Networking.',
            'terms': ['Fa2019', 'Sp2020', 'Su2020', 'Fa2020']
        }
        networking_course = Course.objects.create(**networking_course)
        networking_course.save()

        test_coreq = {
            'course_id': networking_course,
            'course_requisite': self.signals_course,
            'requisite_type': 'co'
        }
        test_coreq = Requisite.objects.create(**test_coreq)
        test_coreq.save()

        new_selective = {
            'course_name': 'Intro to Computer Security',
            'course_tag': 'ECE 40400',
            'course_credits': 3,
            'description': 'Intro to Computer Security.',
            'terms': ['Fa2019', 'Sp2020', 'Su2020', 'Fa2020']
        }
        new_selective = Course.objects.create(**new_selective)
        new_selective.save()

        selective_course_tag = {
            'course_id': new_selective,
            'tag_id': self.test_tag_2
        }
        selective_course_tag = CourseTag.objects.create(**selective_course_tag)
        selective_course_tag.save()

        plan_data = {
            'Fa2019': [self.circuits_1_course.course_id],
            'Sp2020': [self.ai_course.course_id],
            'Su2020': [self.dig_systems_course.course_id, self.os_course.course_id, new_selective.course_id],
            'Fa2020': [networking_course.course_id, self.data_structures_course.course_id]
        }

        response = self.client.put(
            reverse('update_plan', kwargs={'user_id': self.test_student.user_id}),
            data=plan_data
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                'degree': {
                    str(self.test_tag_1.tag_id): -4,
                    str(self.test_tag_2.tag_id): 2
                },
                'requisites': {
                    str(self.ai_course.course_id): {
                        'pre': [self.data_structures_course.course_id],
                    },
                    str(self.os_course.course_id): {
                        'pre': [self.data_structures_course.course_id]
                    },
                    str(networking_course.course_id): {
                        'co': [self.signals_course.course_id]
                    }
                }
            }
        )
