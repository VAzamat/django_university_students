from django.urls import path

from materials.apps import MaterialsConfig
from materials.views import MaterialListView, MaterialDetailView, MaterialUpdateView, MaterialCreateView


app_name = MaterialsConfig.name

urlpatterns = [
    path("material/", MaterialListView.as_view(), name='list'),
    path("material/<int:pk>/", MaterialDetailView.as_view(), name='detail'),
    path("material/update/<int:pk>/", MaterialUpdateView.as_view(), name='update'),
    path("material/create/", MaterialCreateView.as_view(), name='create'),
]