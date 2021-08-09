from django.contrib import admin
from django.urls import path
from .views import loginview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', loginview, name='login'),
]