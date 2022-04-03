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


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'tag_id',
            'degree_id',
            'name',
            'rule'
        )


class CourseTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseTag
        fields = (
            'course_tag_id',
            'tag_id',
            'course_id'
        )


class RequisiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requisite
        fields = (
            'requisite_id',
            'course_id',
            'course_requisites',
            'requisite_type'
        )
