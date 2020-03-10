from django.urls import path

from . import views

urlpatterns = [
    path('/register', views.RegisterCV.as_view(), name="register"),
    path('/registered', views.RegisteredTV.as_view(), name='registered'),
]