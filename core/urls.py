

from unicodedata import name
from django.urls import path

from core.views import log_in, index, register, feed


urlpatterns = [
	path('', index, name="home" ),
	path('feed/', feed, name="feed" ),
	path('register/', register, name='register'),
	path('login', log_in, name="login"),

]