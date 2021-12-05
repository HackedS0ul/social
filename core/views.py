from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import RegisterForm

def index(request):
	return render(request, 'index.html')




def feed(request):
	return render(request, 'feed.html')



def register(request):
	form = RegisterForm(request.POST)

	if form.is_valid():
		form.save()
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password1')
		user = authenticate(username=username, password=password)
		login(request, user)
		return redirect('feed')
	else:
		form = RegisterForm()



	return render(request, 'register.html', {'form':form})