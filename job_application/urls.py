from django.urls import path
from . import views

urlpatterns = [
    path('', views.job, name='job'),
    path('about/', views.about, name='about')
]
