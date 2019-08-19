from django.shortcuts import render,redirect,render_to_response
from .models import Movies,Signup,Theatre,Booking
from .forms import Moviesform,Signupform,Loginform,Moviesform,Theatreform,Bookingform
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'home.html')
def Sign(request):
    form = Signupform()
    if request.method =='POST':
        form = Signupform(request.POST)
        if form.is_valid():
            form.save()   
        return redirect(home)
    return render(request,'signup.html',{'form':form})

def login(request):
    form = Loginform()
    if request.method == 'POST':
        form= Loginform(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')

            log = Signup.objects.filter(email=email,password=password)
            if not log:
                return render(request,'login.html')
            else:
                return redirect(home)
        else:
            return render(request,'login.html',{'form':form})
    return render(request,'login.html',{'form':form})

def movie(request):
    form = Moviesform()
    if request.method == 'POST':
        form = Moviesform(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'movier.html',{"msg":"details successfully submited"})
    return render(request,'movier.html',{'form':form})

def mlist(request):
    mvlist = Movies.objects.all()
    return render(request,"mlist.html",{'form':mvlist})

def theatre(request):
    form = Theatreform()
    if request.method == 'POST':
        form = Theatreform(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'theatre.html',{"msg":"details successfully submited"})
    return render(request,'theatre.html',{'form':form})



def thlist(request):
    tlist = Theatre.objects.all()
    return render(request,"thlist.html",{'form':tlist})





def booking(request):
    form = Bookingform()
    if request.method == 'POST':
        form = Bookingform(request.POST)
        if form.is_valid():
            form.save()
            return redirect(ticket)
    return render(request,'book.html',{'form':form})


    

def ticket(request):
    tick = Booking.objects.all()
    return render(request,"blist.html",{'form':tick})