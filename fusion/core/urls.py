from django.urls import path

from core.views import IndexView, View404

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('404/', View404.as_view(), name='404'),
]
