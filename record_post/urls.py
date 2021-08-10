from django.urls import path

from . import views


app_name = 'record_post'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
]