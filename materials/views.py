from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import  CreateView, ListView, DetailView, UpdateView, DeleteView


from materials.models import Material

# Create your views here.

class MaterialListView(ListView):
    model = Material

class MaterialDetailView(DetailView):
    model = Material

class MaterialUpdateView(UpdateView):
    model = Material
    fields = ('title', "body",)
    template_name = "materials/material_update.html"
    success_url = reverse_lazy('materials:list')

class MaterialCreateView(CreateView):
    model = Material
    fields = ('title', "body",)
    template_name = "materials/material_update.html"
    success_url = reverse_lazy('materials:list')

class MaterialDeleteView(DeleteView):
    model = Material
    success_url = reverse_lazy('materials:list')