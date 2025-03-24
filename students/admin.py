from django.contrib import admin

from students.models import Student, Subject

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'patronymic','email')
    list_filter = ('is_active',)
    search_fields = ('first_name', 'last_name', 'patronymic')

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title','description')
    search_fields = ('title', )
