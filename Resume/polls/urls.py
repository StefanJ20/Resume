from django.urls import path
from . import views  # type: ignore

urlpatterns = [
    path("", views.index, name="index"),
    path("letter/", views.letter, name="letter"),
]