from django.urls import path

from . import views

urlpatterns = [
    path("0/<int:value>", views.index, name="index"),
    path("1/", views.index2, name="index2"),
    path("2/", views.index3, name="index3"),
]