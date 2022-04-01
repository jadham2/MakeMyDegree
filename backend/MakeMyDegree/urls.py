from django.urls import path

from . import views

urlpatterns = [
    path(route='users', view=views.create_get_users, name='create_get_users'),
    path(route='users/<int:user_id>', view=views.detail_user, name='detail_user'),
    path(route='degrees', view=views.create_get_degrees, name='create_get_degrees'),
    path(route='degrees/<int:degree_id>', view=views.detail_degree, name='detail_degree'),
    path(route='courses', view=views.create_get_courses, name='create_get_courses'),
    path(route='courses/<int:course_id>', view=views.detail_course, name='detail_course'),
    path(route='tags', view=views.create_get_tags, name='create_get_tags'),
    path(route='tags/<int:tag_id>', view=views.detail_tags, name='detail_tags'),
    path(route='course_tags', view=views.create_get_courses_tags, name='create_get_courses_tags'),
    path(route='course_tags/<int:course_tag_id>', view=views.detail_course_tags, name='detail_course_tags')
]
