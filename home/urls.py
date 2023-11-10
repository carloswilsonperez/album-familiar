from django.urls import path
from  .views import (
    home, family
)

urlpatterns = [
    path("", home, name="home"),
    path("gallery/", family, name="family"),
]
