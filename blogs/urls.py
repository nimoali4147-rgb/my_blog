from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('home', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('blogs', views.blogs, name='blogs'),
    path('blogs/<slug:slug>', views.blog_detail, name='blog_detail'),
]