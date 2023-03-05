from django.urls import path
from . import views

urlpatterns = [
     path("", views.HomePage, name='home'),
     path("gpa/", views.semester_gpa, name='gpa'),
     path('gpa/courseNum/', views.gpaHome, name='gpahome'),
]