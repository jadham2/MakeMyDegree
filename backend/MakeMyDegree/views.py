from hashlib import sha256
from sys import api_version

from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from MakeMyDegree.models import *
from MakeMyDegree.serializers import *


@api_view(['GET', 'POST'])
@csrf_exempt
def create_get_users(request) -> Response:
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        data = request.data
        data['password'] = sha256(data['password'].encode()).hexdigest()
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def detail_user(request, user_id) -> Response:
    try:
        queried_user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(queried_user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = UserSerializer(queried_user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        queried_user.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
@csrf_exempt
def create_get_courses(request) -> Response:
    if request.method == 'GET':
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        data = request.data
        serializer = CourseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def detail_course(request, course_id) -> Response:
    try:
        queried_course = Course.objects.get(pk=course_id)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CourseSerializer(queried_course)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = CourseSerializer(queried_course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        queried_course.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
@csrf_exempt
def create_get_degrees(request) -> Response:
    if request.method == 'GET':
        degrees = Degree.objects.all()
        serializer = DegreeSerializer(degrees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        data = request.data
        serializer = DegreeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def detail_degree(request, degree_id) -> Response:
    try:
        queried_degree = Degree.objects.get(pk=degree_id)
    except Degree.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DegreeSerializer(queried_degree)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = DegreeSerializer(queried_degree, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        queried_degree.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def create_get_tags(request) -> Response:
    if request.method == 'GET':
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        data = request.data
        serializer = TagSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def detail_tag(request, tag_id) -> Response:
    try:
        queried_tag = Tag.objects.get(pk=tag_id)
    except Tag.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TagSerializer(queried_tag)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = TagSerializer(queried_tag, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        queried_tag.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def create_get_course_tags(request) -> Response:
    if request.method == 'GET':
        course_tags = CourseTag.objects.all()
        serializer = CourseTagSerializer(course_tags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        data = request.data
        serializer = CourseTagSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def detail_course_tag(request, course_tag_id) -> Response:
    try:
        queried_course_tag = CourseTag.objects.get(pk=course_tag_id)
    except CourseTag.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CourseTagSerializer(queried_course_tag)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = CourseTagSerializer(queried_course_tag, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        queried_course_tag.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def create_get_requisites(request) -> Response:
    if request.method == 'GET':
        requisites = Requisite.objects.all()
        serializer = RequisiteSerializer(requisites, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        data = request.data
        serializer = RequisiteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def detail_requisite(request, requisite_id) -> Response:
    try:
        queried_requisite = Requisite.objects.get(pk=requisite_id)
    except Requisite.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RequisiteSerializer(queried_requisite)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = RequisiteSerializer(queried_requisite, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        queried_requisite.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_plan(request, user_id) -> Response:
    """
    We want to grab the user's plan given their user_id.
    This plan is a json object with the following format:
    { "Term 1": [ course_ids ], "Term 2": [ course_ids ]}
    where the keys and values are placeholders. A real example may
    look like this:
    { "Fa2019": [123, 551, 2, 3], "Sp2020": [234, 4, 3, 124]}
    """

    try:
        queried_user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    queried_user.curr_plan = request.data
    queried_user.save()

    plan = dict(queried_user.curr_plan.lists())
    for term in plan:
        for i, course_id in enumerate(plan[term]):
            try:
                queried_course = Course.objects.get(pk=int(course_id))
            except Course.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            plan[term][i] = queried_course

    # Get all the tags associated with the user's degree.
    degree_tags = Tag.objects.filter(degree=queried_user.degree)

    # Create an audit response to track conflicting requisites and
    # missing degree requirements based on tags.
    audit_response = {
        "requisites": {},
        "degree": {
            x.tag_id: 0 for x in degree_tags
        }
    }

    # Iterate through each term of the plan and check term by term for missing pre/co requisites.
    # If a course is missing a pre/co requisite, add it to the audit response.
    # For each course, increment the credit of the tag associated with the course.
    term_sort_map = {'Sp': '1', 'Su': '2', 'Fa': '3'}
    # The idea for requisite is to keep a moving set of encountered courses as we go through
    # plans sequentially.
    courses_encountered = set()
    for term in sorted(plan, key=lambda x: x[2:] + term_sort_map[x[:2]]):
        current_courses = set(plan[term])
        for course in plan[term]:
            # First, increment the credit of each tag associated with the course.
            # This will be included in the audit response.
            for course_tag in CourseTag.objects.select_related('tag_id').filter(course_id=course):
                audit_response['degree'][course_tag.tag_id.tag_id] += course.course_credits

            # Then, check if the course has any pre/co requisite violations.
            # If so, add it to the audit response.
            for requisite in Requisite.objects.filter(course_id=course):
                if requisite.requisite_type == 'pre':
                    if requisite.course_requisite not in courses_encountered:
                        if course.course_id not in audit_response['requisites']:
                            audit_response['requisites'][course.course_id] = {'pre': []}
                        audit_response['requisites'][course.course_id]['pre'].append(requisite.course_requisite.course_id)
                elif requisite.requisite_type == 'co':
                    if requisite.requisite_id not in courses_encountered or current_courses:
                        if course.course_id not in audit_response['requisites']:
                            audit_response['requisites'][course.course_id] = {'co': []}
                        audit_response['requisites'][course.course_id]['co'].append(requisite.course_requisite.course_id)

        # Once we finish with the term we are on, add the term's courses
        # to the overall set for future pre-requisites checks.
        courses_encountered.update(current_courses)

    return Response(audit_response, status.HTTP_200_OK)
