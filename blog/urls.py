from django.urls import path

from . import views

urlpatterns = [
    path('', views.blogPage, name='blog_page'),
]