from django.urls import reverse
from MakeMyDegree.models import *
import json
from rest_framework import status
from rest_framework.test import APIClient
import re


# insert all Purdue courses
def all_purdue_courses_setup():
    with open("MakeMyDegree/fixture/purdue_all_courses.json", "r") as f:
        all_courses = json.load(f)
    with open("MakeMyDegree/fixture/ece_tags.json", "r") as f:
        ece_tags_content = f.read()
    for a_course in all_courses:
        if ("ECE 20001" <= a_course['course_tag'] <= "ECE 60000") or (a_course["course_tag"] in ece_tags_content) or (a_course["course_tag"] == 'EAPS 10600'):
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
    all_courses = dict()
    for a_course in get_courses_resp:
        all_course_ids[a_course["course_tag"]] = a_course["course_id"]
        all_courses[a_course["course_tag"]] = {k: v for k, v in a_course.items() if k not in ['description', 'terms']}
    return all_course_ids, all_courses


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
                        'requisite_type': ece_reqs[a_req][a_req_course].lower()
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

    # insert all other degrees
    with open("MakeMyDegree/fixture/purdue_degrees.txt", "r") as f:
        content = f.readlines()
    degree_pattern = re.compile(r"(.+),\s([A-Z]+)")
    for i, a_line in enumerate(content):
        try:
            a_line = a_line.rstrip()
            result = degree_pattern.search(a_line)
            a_degree = {
                'degree_type': result.group(2),
                'degree_name': result.group(1),
                'school': 'ENGR',
                'term': 'Fa2019'
            }
            client = APIClient()
            client.post(
                reverse('create_get_degrees'),
                data=a_degree,
                format='json'
            )
        except Exception:
            print(f"Degree Line {i} cannot be parsed: {a_line.rstrip()}")

    # insert all ece degree tags, along with the course tags
    with open("MakeMyDegree/fixture/ece_tags.json", "r") as f:
        ece = json.load(f)
    for a_tag in ece:
        a_ece_tag_data = {
            'degree': ece_degree_id,
            'name': a_tag["tag_name"],
            'rule': '>= ' + str(a_tag["credits"])
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
def test_user_setup(ece_degree_id, all_courses):
    model_plan = {
        'Fa2019': ['SPAN 10100', 'ENGR 13100', 'CS 15900', 'MA 16500', 'PHYS 17200', 'COM 11400'],
        'Sp2020': ['ENGR 13200', 'MA 16600', 'PHYS 27200', 'PSY 12000', 'ENGL 10600', ],
        'Su2020': [],
        'Fa2020': ['MA 26100', 'ECE 20001', 'ECE 20007', 'ECE 26400', 'CHM 11500'],
        'Sp2021': ['MA 26600', 'ECE 20002', 'ECE 27000', 'ECE 29401', 'PSY 20000'],
        'Su2021': [],
        'Fa2021': ['MA 26500', 'ECE 36800', 'ECE 30100', 'ECE 33700', 'ECE 39401'],
        'Sp2022': ['ECE 36200', 'ECE 30200', 'ECE 46900', 'ECE 20875', 'ME 20000'],
        'Su2022': [],
        'Fa2022': ['ECE 36900', 'ECE 57000', 'ECE 49401', 'ECON 25100', 'CHM 11600'],
        'Sp2023': ['PSY 22200', 'ECE 40400', 'ECE 46800', 'ECE 49595', 'EAPS 10600']
    }
    test_student_data = {
        'name': 'test',
        'password': '123456',
        'degree': ece_degree_id,
        'curr_plan': {k: [all_courses[x] for x in v] for k, v in model_plan.items()}
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
    all_course_ids, all_courses = get_all_course_ids()
    all_purdue_requisites_setup(all_course_ids)
    ece_degree_id = ece_degree_setup(all_course_ids)
    test_user_setup(ece_degree_id, all_courses)
