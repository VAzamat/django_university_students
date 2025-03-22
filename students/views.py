from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import  CreateView, ListView, DetailView, UpdateView, DeleteView
from students.models import Student



# Create your views here.

class StudentDetailView(DetailView):
    model = Student
    #template_name = "students/student_detail.html"

class StudentListView(ListView):
    model = Student


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


def toggle_activity(request, pk):
    student_item = get_object_or_404(Student,pk=pk)
    student_item.is_active = not student_item.is_active
    student_item.save()

    return redirect( reverse_lazy('students:list') )
