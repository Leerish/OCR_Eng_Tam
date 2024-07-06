# translator/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.translate, name='translate'),
    path('download/<path:path>', views.download, name='download'),
]
