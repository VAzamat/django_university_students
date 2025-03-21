from django.urls import path

from materials.apps import MaterialsConfig
from materials.views import MaterialListView, MaterialDetailView


app_name = MaterialsConfig.name

urlpatterns = [
    path("material/", MaterialListView.as_view(), name='list'),
    path("material/<int:pk>/", MaterialDetailView.as_view(), name='detail'),
]