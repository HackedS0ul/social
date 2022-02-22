from audioop import reverse
from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseRedirect
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



def log_in(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('feed'))
			else:
				return HttpResponse("Your account is inactive")

		return HttpResponse("Please try again your username or password is incorrect!")


	return render(request, 'login.html', {})


	

