from django.urls import path
from students.views import home

from students.apps import StudentsConfig

app_name = StudentsConfig.name

urlpatterns = [
    path("", home, name='home'),
]