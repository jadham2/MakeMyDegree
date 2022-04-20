from django.urls import path

from . import views

urlpatterns = [
    path(route='users', view=views.create_get_users, name='create_get_users'),
    path(route='users/<int:user_id>', view=views.detail_user, name='detail_user'),
    path(route='degrees', view=views.create_get_degrees, name='create_get_degrees'),
    path(route='degrees/<int:degree_id>', view=views.detail_degree, name='detail_degree'),
    path(route='degrees/<int:degree_id>/tags', view=views.fetch_degree_tags, name='fetch_degree_tags'),
    path(route='courses', view=views.create_get_courses, name='create_get_courses'),
    path(route='courses/<int:course_id>', view=views.detail_course, name='detail_course'),
    path(route='tags', view=views.create_get_tags, name='create_get_tags'),
    path(route='tags/<int:tag_id>', view=views.detail_tag, name='detail_tag'),
    path(route='course_tags', view=views.create_get_course_tags, name='create_get_course_tags'),
    path(route='course_tags/<int:course_tag_id>', view=views.detail_course_tag, name='detail_course_tag'),
    path(route='requisites', view=views.create_get_requisites, name='create_get_requisites'),
    path(route='requisites/<int:requisite_id>', view=views.detail_requisite, name='detail_requisite'),
    path(route='users/<int:user_id>/update', view=views.update_plan, name='update_plan'),
    path(route='login', view=views.login_user, name='login_user')
]
