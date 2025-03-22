from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import  CreateView, ListView, DetailView, UpdateView, DeleteView
from students.models import Student



# Create your views here.

class StudentDetailView(DetailView):
    model = Student
    #template_name = "students/student_detail.html"

class StudentListView(ListView):
    model = Student
    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_active=True)
        return queryset

class StudentCreateView(CreateView):
    model = Student
    fields = ("last_name", 'first_name', "patronymic", "is_active", "avatar")
    success_url = reverse_lazy('students:list')

class StudentUpdateView(UpdateView):
    model = Student
    fields = ("last_name", 'first_name', "patronymic", "is_active", "avatar")
    def get_success_url(self):
        return reverse('students:detail', args=[self.kwargs.get('pk')] )

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list')