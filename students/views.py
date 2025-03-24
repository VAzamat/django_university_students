from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import  CreateView, ListView, DetailView, UpdateView, DeleteView
from students.models import Student, Subject
from students.forms import StudentForm, SubjectForm


# Create your views here.

class StudentDetailView(DetailView):
    model = Student
    #template_name = "students/student_detail.html"

class StudentListView(ListView):
    model = Student


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    #fields = ("last_name", 'first_name', "patronymic", "is_active", "avatar")
    success_url = reverse_lazy('students:list')

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    #fields = ("last_name", 'first_name', "patronymic", "is_active", "avatar")
    def get_success_url(self):
        return reverse('students:detail', args=[self.kwargs.get('pk')] )

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SubjectFormset = inlineformset_factory(Student, Subject, form=SubjectForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = SubjectFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = SubjectFormset(instance=self.object)

        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)



class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list')


def toggle_activity(request, pk):
    student_item = get_object_or_404(Student,pk=pk)
    student_item.is_active = not student_item.is_active
    student_item.save()

    return redirect( reverse_lazy('students:list') )
