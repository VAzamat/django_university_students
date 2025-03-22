from django.urls import path
from students.views import StudentDetailView, StudentListView, StudentUpdateView, StudentCreateView, StudentDeleteView

from students.apps import StudentsConfig

app_name = StudentsConfig.name

urlpatterns = [
    path("",                  StudentListView.as_view(), name='list'),
    path("student/<int:pk>/", StudentDetailView.as_view(), name='detail'),
    path("student/create/", StudentCreateView.as_view(), name='create'),
    path("student/update/<int:pk>/", StudentUpdateView.as_view(), name='update'),
    path("student/delete/<int:pk>/", StudentDeleteView.as_view(), name='delete'),
]