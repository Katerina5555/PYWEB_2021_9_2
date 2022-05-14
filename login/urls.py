from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.LoginIndexView.as_view()),

    ]