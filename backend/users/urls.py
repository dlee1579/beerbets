from django.urls import include, path
from rest_framework import routers
from . import views
from .api import urls

router = routers.DefaultRouter()

urlpatterns = [
    path("", views.index, name="index"),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(urls)),
    path('register', views.register, name='register')
]