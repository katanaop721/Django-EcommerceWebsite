from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="shopl"),
path("about/", views.about, name="aboutus"),
path("contact/", views.contact, name="contactus"),
path("tracker/", views.track, name="tracker"),
path("search/", views.search, name="search"),
path("product/<int:myid>", views.proview, name="proview"),
path("checkout", views.chout, name="chout"),
path("handlerequest/", views.handlerequest, name="HandleRequest"),
]
