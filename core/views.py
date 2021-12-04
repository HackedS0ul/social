from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	return render(request, 'index.html')




def feed(request):
	return render(request, 'feed.html')