from django.urls import path
from  .views import (
    home, about, gallery, contact, family, pictures2004, pictures2005
)

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("gallery/", gallery, name="gallery"),
    path("/", family, name="family"),
    path("contact/", contact, name="contact"),
    path("pictures2004/", pictures2004, name="pictures2004"),
    path("pictures2005/", pictures2005, name="pictures2005")
]
