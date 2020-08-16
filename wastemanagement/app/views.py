from django.shortcuts import render,HttpResponse, HttpResponseRedirect, redirect, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import Profile,Form1model
from django.db.models import Sum
from .forms import Form1
from django.views.decorators.csrf import csrf_protect

def index(request):
    return render(request,'app/index.html',{})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'app/signup.html', {'form': form})

def login_view(request):
	message='Log In'
	if request.method=='POST':
		_username=request.POST['username']
		_password=request.POST['password']
		user=authenticate(username=_username,password=_password)
		if user is not None:
			if user.is_active:
				login(request,user)
				return redirect('index')
			else:
				message='Not Activated'
		else:
			message='Invalid Login'
	context={'message':message}
	return render(request,'app/login.html',context)

def logout_view(request):
	logout(request)
	return redirect('index')

def form1submit(request):
	if request.method=='POST':
		form=Form1(request.POST)
		if form.is_valid():
			p = form.save(commit=False)
			p.save()
			return redirect('index')
	else:
		form=Form1()
	return render(request,'app/form1.html',{'form':form})
@csrf_protect
def dashboard(request):
	f = Form1model.objects.all()
	total_num_trips = f.aggregate(Sum('num_trips'))
	quantity = f.aggregate(Sum('quantity'))
	if(request.method == 'POST'):
		location = request.POST['location'].lower()
		f = f.filter(location = location)
		total_num_trips = f.aggregate(Sum('num_trips'))
		quantity = f.aggregate(Sum('quantity'))
		return render(request,'app/dashboard.html',{'data':f,'trips':total_num_trips,'qty':quantity})	
	return render(request,'app/dashboard.html',{'data':f,'trips':total_num_trips,'qty':quantity})