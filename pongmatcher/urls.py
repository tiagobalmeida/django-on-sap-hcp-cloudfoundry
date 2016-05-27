from django.conf.urls import url
from pongmatcher import views

urlpatterns = [
        url(r'^hello$', views.hello)
]
