from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('students.urls',namespace='students')),
    path("", include('materials.urls', namespace='materials')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
admin.AdminSite.site_header = 'Моя админка'
admin.AdminSite.index_title = 'Главная страница настройки администрирования приложения'