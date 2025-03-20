from django.urls import path
from students.views import index

from students.apps import StudentsConfig

app_name = StudentsConfig.name

urlpatterns = [
    path("", index, name='index'),
]
