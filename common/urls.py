from django.urls import path

from . import views

urlpatterns = [
    path('common/', views.HelloView.as_view()),
    path('', views.IndexView.as_view())

    ]