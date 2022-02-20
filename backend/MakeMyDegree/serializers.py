from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'user_id',
            'name',
            'password',
            'email',
            'degree',
            'curr_plan'
        )

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            'course_id',
            'course_name',
            'course_tag',
            'course_credits',
            'description',
            'terms'
        )

class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Degree
        fields = (
            'degree_id',
            'degree_type',
            'degree_name',
            'school',
            'term'
        )
