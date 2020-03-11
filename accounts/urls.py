from django.urls import path, include

from . import views


urlpatterns = [
    path('/register', views.RegisterCV.as_view(), name="register"),
    path('/registered', views.RegisteredTV.as_view(), name='registered'),
    path('', include('django.contrib.auth.urls')),
]