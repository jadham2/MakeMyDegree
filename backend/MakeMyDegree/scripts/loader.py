from django.urls import reverse
from MakeMyDegree.models import *
import json
from rest_framework import status
from rest_framework.test import APIClient


# insert all Purdue courses
def all_purdue_courses_setup():
    with open("MakeMyDegree/fixture/purdue_all_courses.json", "r") as f:
        all_courses = json.load(f)
    for a_course in all_courses:
        if "ECE 20001" <= a_course['course_tag'] <= "ECE 60000":
            client = APIClient()
            course_resp = client.post(
                reverse('create_get_courses'),
                data=a_course,
                format='json'
            )
            if (course_resp.status_code == status.HTTP_400_BAD_REQUEST):
                print(a_course)


def get_all_course_ids():
    client = APIClient()
    get_courses_resp = client.get(
        reverse('create_get_courses'),
        format='json'
    )
    get_courses_resp = get_courses_resp.json()
    all_course_ids = dict()
    for a_course in get_courses_resp:
        all_course_ids[a_course["course_tag"]] = a_course["course_id"]
    return all_course_ids


# insert all Purdue course pre and co-requisites
# TODO: So far only ECE requisites are available
def all_purdue_requisites_setup(all_course_ids):
    with open("MakeMyDegree/fixture/ece_requisites.json", "r") as f:
        ece_reqs = json.load(f)
    client = APIClient()
    for a_req in ece_reqs:
        if a_req in all_course_ids:
            for a_req_course in ece_reqs[a_req]:
                if (a_req_course in all_course_ids):
                    test_requisite_data = {
                        'course_id': all_course_ids[a_req],
                        'course_requisite': all_course_ids[a_req_course],
                        'requisite_type': ece_reqs[a_req][a_req_course]
                    }
                    requisite_resp = client.post(
                        reverse('create_get_requisites'),
                        data=test_requisite_data,
                        format='json'
                    )
                    if (requisite_resp.status_code == status.HTTP_400_BAD_REQUEST):
                        print(test_requisite_data)


# insert a sample degree
def ece_degree_setup(all_course_ids):
    # insert a ece degree
    ece_degree = {
        'degree_type': 'BS',
        'degree_name': 'Computer Engineering',
        'school': 'ENGR',
        'term': 'Fa2019'
    }
    client = APIClient()
    ece_resp = client.post(
        reverse('create_get_degrees'),
        data=ece_degree,
        format='json'
    )
    assert (ece_resp.status_code == status.HTTP_201_CREATED)
    ece_degree_id = ece_resp.json()["degree_id"]

    # insert all ece degree tags, along with the course tags
    with open("MakeMyDegree/fixture/ece_tags.json", "r") as f:
        ece = json.load(f)
    for a_tag in ece:
        a_ece_tag_data = {
            'degree': ece_degree_id,
            'name': a_tag["tag_name"],
            'rule': '>=' + str(a_tag["credits"])
        }
        client = APIClient()
        tag_resp = client.post(
            reverse('create_get_tags'),
            data=a_ece_tag_data,
            format='json'
        )
        if (tag_resp.status_code == status.HTTP_400_BAD_REQUEST):
            print(a_ece_tag_data)
        # update the course tags table
        for a_course in a_tag["course_list"]:
            try:
                test_course_tag_data = {
                    'course_id': all_course_ids[a_course],
                    'tag_id': tag_resp.json()["tag_id"]
                }
                post_course_tag_resp = client.post(
                    reverse('create_get_course_tags'),
                    data=test_course_tag_data,
                    format='json'
                )
                if (post_course_tag_resp.status_code == status.HTTP_400_BAD_REQUEST):
                    print(test_course_tag_data)
            except Exception as e:
                print(e)
    return ece_degree_id


# insert a test user
def test_user_setup(ece_degree_id, all_course_ids):
    test_student_data = {
        'name': 'John XYZ',
        'password': '123456',
        'email': 'xyz@purdue.edu',
        'degree': ece_degree_id,
        'curr_plan': {
            'Fa2019': [all_course_ids["CS 15900"], all_course_ids["ECE 20001"], all_course_ids["ECE 20007"]],
            'Sp2020': [all_course_ids["ECE 26400"], all_course_ids["ECE 20875"]],
            'Su2020': [all_course_ids["ECE 36800"]],
            'Fa2020': [],
            'Sp2021': [],
            'Su2021': []
        }
    }
    client = APIClient()
    user_resp = client.post(
        reverse('create_get_users'),
        data=test_student_data,
        format='json'
    )
    if (user_resp.status_code == status.HTTP_400_BAD_REQUEST):
        print(test_student_data)


def run():
    all_purdue_courses_setup()
    all_course_ids = get_all_course_ids()
    all_purdue_requisites_setup(all_course_ids)
    ece_degree_id = ece_degree_setup(all_course_ids)
    # test_user_setup(ece_degree_id, all_course_ids)
