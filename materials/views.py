from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import  CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from materials.models import Material

# Create your views here.

class MaterialListView(ListView):
    model = Material

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset

class MaterialDetailView(DetailView):
    model = Material

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object

class MaterialUpdateView(UpdateView):
    model = Material
    fields = ('title', "body", "is_published")
    template_name = "materials/material_update.html"
    success_url = reverse_lazy('materials:list')

    def form_valid(self, form):
        if form.is_valid():
            new_item = form.save()
            new_item.slug = slugify(new_item.title)
            new_item.save()
        return super().form_valid(form)

class MaterialCreateView(CreateView):
    model = Material
    fields = ('title', "body", "is_published")
    template_name = "materials/material_update.html"
    success_url = reverse_lazy('materials:list')

    def form_valid(self, form):
        if form.is_valid():
            new_item = form.save()
            new_item.slug = slugify(new_item.title)
            new_item.save()
        return super().form_valid(form)

class MaterialDeleteView(DeleteView):
    model = Material
    success_url = reverse_lazy('materials:list')