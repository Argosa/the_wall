from django.urls import path
from . import views

urlpatterns = [
    path('wall/', views.wall),
    path('process_post', views.process_post),
]