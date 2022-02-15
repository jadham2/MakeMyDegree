from hashlib import sha256

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from MakeMyDegree.models import User
from MakeMyDegree.serializers import *


@csrf_exempt
def create_user(request) -> JsonResponse:
    if request.method == 'POST':
        data = JSONParser().parse(request)
        data['password'] = sha256(data['password'].encode()).hexdigest()
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=201)
        return JsonResponse(data=serializer.errors, status=400)


@csrf_exempt
def create_degree(request) -> JsonResponse:
    if request.method == 'GET':
        return JsonResponse(data={}, status=200)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DegreeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=201)
        return JsonResponse(data=serializer.errors, status=400)
