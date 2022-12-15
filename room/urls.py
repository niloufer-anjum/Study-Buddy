from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="rooms"),
    path('<slug:slug>', views.room, name="room"),
]
