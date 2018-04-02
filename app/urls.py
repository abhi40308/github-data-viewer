# app/urls.py

from django.conf.urls import url

from app import views

urlpatterns = [
  url(r'^$', views.profile, name='profile'),
]