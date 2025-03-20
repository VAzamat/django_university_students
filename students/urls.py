from django.urls import path
from students.views import student_list, student_detail

from students.apps import StudentsConfig

app_name = StudentsConfig.name

urlpatterns = [
    path("", student_list, name='student_list'),
    path("student/<int:pk>/", student_detail, name='student_detail'),
]