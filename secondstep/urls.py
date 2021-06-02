from django.urls import path, include
from .views import helloAPI, printObject

urlpatterns = [
    path("hello/", helloAPI),
    path("res/", printObject),
]