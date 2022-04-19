from django.urls import reverse
from MakeMyDegree.models import *
import json
from rest_framework import status
from rest_framework.test import APIClient

# insert all Purdue courses
def all_purdue_courses_setup():
    with open("MakeMyDegree/fixture/purdue_all_courses.json", "r") as f:
        all_courses = json.load(f)
    all_courses = [a_course["fields"] for a_course in all_courses]
    for a_course in all_courses:
        client = APIClient()
        course_resp = client.post(
                reverse('create_get_courses'),
                data=a_course,
                format='json'
        )
        if (course_resp.status_code == status.HTTP_400_BAD_REQUEST):
            print(a_course)

# insert a sample degree
def ece_degree_setup(self):
    return 
    with open("../../degree_scrape/degrees/ece_tags.pickle", "rb") as f:
        ece = json.load(f)
    for a in ece:
        pass
    compe_degree_data = {
        'degree_type': 'BS',
        'degree_name': 'Computer Engineering',
        'school': 'ECE',
        'term': 'Fa2019'
    }

def run():
    all_purdue_courses_setup()
    ece_degree_setup()
