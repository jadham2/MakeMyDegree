from django.urls import path

from . import views

urlpatterns = [
    path(route='users', view=views.create_user, name='create_get_users'),
    path(route='degrees', view=views.create_degree, name='create_get_degrees')
]
