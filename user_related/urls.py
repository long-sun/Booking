from django.conf.urls import url
from user_related import views

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
]