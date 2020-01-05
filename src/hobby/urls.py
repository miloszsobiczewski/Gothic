from django.conf.urls import url

from .views import download

app_name = "shooting"


urlpatterns = [
    url(r"^download/(?P<pk>[-\w]+)/$", download, name="download"),
]
