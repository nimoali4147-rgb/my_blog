from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('subscribe', views.subscribe, name='subscribe'),
    path('blogs', views.blogs, name='blogs'),
    path('blogs/create/', views.create_post, name='create_post'),
    path('blogs/<slug:slug>/edit/', views.edit_post, name='edit_post'),
    path('blogs/<slug:slug>/', views.blog_detail, name='blog_detail'),
]