from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('SuperAdmin/', admin.site.urls),
    path('', include('app.urls')),
]