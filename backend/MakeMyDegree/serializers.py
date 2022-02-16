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
