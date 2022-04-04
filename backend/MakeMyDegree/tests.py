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
            'degree_id': self.compe_degree.degree_id,
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
        self.assertEqual(tag_resp['degree_id'], self.compe_degree.degree_id)

    def test_create_tag_invalid_degree(self):
        test_tag_data = {
            'degree_id': '25325234',
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
            'degree_id': self.compe_degree,
            'name': 'General Education',
            'rule': '>= 17'
        }
        test_tag = Tag.objects.create(**test_tag_data)
        test_tag.save()

        test_tag_data = {
            'degree_id': self.compe_degree,
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
            'degree_id': self.compe_degree,
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
        self.assertEqual(get_tag_resp['degree_id'], self.compe_degree.degree_id)

    def test_get_tag_id_invalid(self):
        get_tag_resp = self.client.get(
            reverse('detail_tag', kwargs={'tag_id': 123132}),
            format='json'
        )

        self.assertEqual(get_tag_resp.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_tag_id_valid(self):
        test_tag_data = {
            'degree_id': self.compe_degree,
            'name': 'General Education',
            'rule': '>= 17'
        }
        test_tag = Tag.objects.create(**test_tag_data)
        test_tag.save()

        update_data = {
            'degree_id': self.compe_degree.degree_id,
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
        self.assertEqual(put_tag_resp['degree_id'], self.compe_degree.degree_id)

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
            'degree_id': self.compe_degree,
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
            'degree_id': cs_degree,
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
            degree_id=self.compe_degree,
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
