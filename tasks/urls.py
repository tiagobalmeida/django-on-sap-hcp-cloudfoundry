from django.conf.urls import url
from tasks import views
app_name = 'tasks'
urlpatterns = [
        url(r'^$', views.index, name="index")
]
