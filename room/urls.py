from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name="rooms"),
    re_path(r'(?P<room>[-\w|\W| ]+)/$', views.room, name="room"),
]