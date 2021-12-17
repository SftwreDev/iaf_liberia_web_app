from django.urls import path

from .views.homepage.homepage_views import *


app_name = "applications"

urlpatterns = [
    path("", homepage, name="homepage")
]
