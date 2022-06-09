from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('update', views.update, name='update'),
    path('read/<str:npm>', views.read, name='read'),
]
