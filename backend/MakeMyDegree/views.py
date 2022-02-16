from hashlib import sha256

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import JSONParser

from MakeMyDegree.models import *
from MakeMyDegree.serializers import *


@csrf_exempt
def create_user(request) -> JsonResponse:
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(data=serializer.data, safe=False, status=status.HTTP_200_OK)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        data['password'] = sha256(data['password'].encode()).hexdigest()
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def create_degree(request) -> JsonResponse:
    if request.method == 'GET':
        degrees = Degree.objects.all()
        serializer = DegreeSerializer(degrees, many=True)
        return JsonResponse(data=serializer.data, safe=False, status=status.HTTP_200_OK)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DegreeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
