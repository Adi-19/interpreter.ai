from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('comingSoon/', views.under, name="under"),
    path('submitted/', views.submitForm, name="submitForm")
]