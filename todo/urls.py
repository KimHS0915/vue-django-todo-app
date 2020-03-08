from django.urls import path

from . import views

app_name = 'todo'

urlpatterns = [
    path('vonly/', views.TodoVueOnlyTV.as_view(), name='vonly'),

    path('donly/create/', views.TodoCV.as_view(), name='dcreate'),
    path('donly/list/', views.TodoLV.as_view(), name='dlist'),
    path('donly/<int:pk>/delete/', views.TodoDelV.as_view(), name='ddelete'),

    path('mixin/', views.TodoMOMCV.as_view(), name='mixin'),
    path('<int:pk>/delete2/', views.TodoDelV2.as_view(), name='delete2'),

    path('', views.TodoTV.as_view(), name='index')
]