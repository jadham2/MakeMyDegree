from django.urls import path

from . import views

urlpatterns = [
    path(route='users', view=views.create_get_users, name='create_get_users'),
    path(route='degrees', view=views.create_get_degrees, name='create_get_degrees'),
    path(route='users/<int:user_id>', view=views.detail_user, name='detail_user'),
    path(route='courses', view=views.create_get_courses, name='create_get-courses'),
    path(route='courses/<int:course_id>', view=views.detail_course, name='detail_course')
]
