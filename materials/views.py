from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import  CreateView, ListView, DetailView


from materials.models import Material

# Create your views here.

class MaterialListView(ListView):
    model = Material

class MaterialDetailView(DetailView):
    model = Material

class MaterialCreateView(CreateView):
    model = Material
    fields = ('title', 'body',)
    success_url = reverse_lazy('materials:list')