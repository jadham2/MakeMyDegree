from django.urls import reverse
from MakeMyDegree.models import *
import json
# from rest_framework.request import HttpRequest
# from rest_framework.test import APIRequestFactory
from rest_framework import status
from rest_framework.test import APIClient
from time import sleep

# insert all Purdue courses
def all_purdue_courses_setup():
    with open("MakeMyDegree/fixture/purdue_all_courses.json", "r") as f:
        all_courses = json.load(f)
    all_courses = [a_course["fields"] for a_course in all_courses]
    for a_course in all_courses:
        course_resp = None
        while ((course_resp) and (course_resp.status_code == status.HTTP_400_BAD_REQUEST)):
            client = APIClient()
            course_resp = client.post(
                    reverse('create_get_courses'),
                    data=a_course,
                    format='json'
            )
            # print(course_resp)
            # sleep(0.1)
        # if (course_resp["status_code"] == status.HTTP_201_CREATED):
        #     print(course_resp)


# # insert a sample degree
# def ece_degree_setup(self):
#     with open("../../degree_scrape/degrees/ece_tags.pickle", "rb") as f:
#         ece = pickle.load(f)
#     for a 
#     compe_degree_data = {
#         'degree_type': 'BS',
#         'degree_name': 'Computer Engineering',
#         'school': 'ECE',
#         'term': 'Fa2019'
#     }
#     self.compe_degree = Degree.objects.create(**compe_degree_data)
#     self.compe_degree.save()

#     test_student_data = {
#         'name': 'Jude Lei',
#         'password': 'HelloWorld!@#',
#         'email': 'jadham@purdue.edu',
#         'degree': self.compe_degree,
#         'curr_plan': {}
#     }
#     self.test_student = User.objects.create(**test_student_data)
#     self.test_student.save()
def run():

    all_purdue_courses_setup()