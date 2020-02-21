from django.urls import path
from . import views

urlpatterns = [
    path('wall/', views.wall),
    path('process_post', views.process_post),
    path('process_comment', views.process_comment),
    path('delete_message', views.delete_message),
    path('logout', views.logout),
]