from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process_reg', views.process_reg),
    path('success', views.success),
    path('logout', views.logout),
    path('process_login', views.process_login),
]