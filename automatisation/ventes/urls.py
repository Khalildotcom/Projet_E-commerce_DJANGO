from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("resultats/", views.resultats, name="resultats"),
]