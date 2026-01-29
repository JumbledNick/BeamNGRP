from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm

# Create your views here.
def index(request):
    return render(request, 'core/index.html')
def base(request):
    return render(request, 'core/base.html')
def forum(request):
    return render(request, 'core/forum.html')
def business(request):
    return render(request, 'core/business.html')
def magazine(request):
    return render(request, 'core/magazine.html')
def market(request):
    return render(request, 'core/market.html')
def wiki(request):
    return render(request, 'core/wiki.html')

@login_required
def profile(request):
    return render(request, 'core/profile.html',{
        "user": request.user,
    })

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    
    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html', {'form':form})