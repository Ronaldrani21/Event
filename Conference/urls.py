from django.urls import path

from . import views

app_name = "Conference"

urlpatterns = [
    path('',views.home, name='home'),


]