from django.urls import path

from . import views

urlpatterns = [
    path('', views.About),
    path('contact/', views.Contact),
    path('classes/', views.Classes)

]