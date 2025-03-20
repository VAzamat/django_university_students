from django.shortcuts import render, get_object_or_404

from students.models import Student

# Create your views here.

def student_list(request):
    students = Student.objects.all()

    context = {
        'student_list': students
    }

    return render(request, 'students/student_list.html', context)

def student_detail(request, pk):
    student = get_object_or_404(Student,pk=pk)


    context = {
        'student_item': student
    }

    return render(request, 'students/student_detail.html', context)