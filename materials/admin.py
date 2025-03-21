from django.contrib import admin
from materials.models import Material
from students.templatetags.path_tag_filter import register

# Register your models here.

@admin.register(Material)
class MaterialClass(admin.ModelAdmin):
    list_display = ("title","body",)
    search_fields = ("title",)


