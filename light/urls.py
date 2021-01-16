from .views import MainLight,DetailsLight
from django.contrib import admin
from django.urls import path
urlpatterns = [
    path('',MainLight.as_view(),name = 'list'),
    path('<int:pk>/',DetailsLight.as_view(),name='details')

]