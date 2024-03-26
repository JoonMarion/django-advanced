from django.contrib import admin
from django.urls import path, include
from core import views
from django.conf.urls import handler404


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]

handler404 = views.error_404

