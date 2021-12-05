

from django.urls import path

from . import views


urlpatterns = [
	path('', views.index, name="home" ),
	path('feed/', views.feed, name="feed" ),
	path('register/', views.register, name='register'),

]