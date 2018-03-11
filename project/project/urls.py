from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('notes/', include('notes.urls')),
    path('admin/', admin.site.urls),
]