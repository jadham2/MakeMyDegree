from django.urls import path

from . import views

urlpatterns = [
    path(route='users', view=views.create_user),
    path(route='degrees', view=views.create_degree)
]
