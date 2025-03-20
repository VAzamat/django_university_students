from django.contrib import admin

from students.models import Student

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',)
    list_filter = ('is_active',)
    search_fields = ('first_name', 'last_name',)