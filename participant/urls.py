from django.urls import path, re_path, include
from . import views

urlpatterns = [
    re_path(r'(?P<user>[-\w|\W| ]+)/$', views.profile, name="profile")
    ]