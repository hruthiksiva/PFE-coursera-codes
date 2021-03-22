from django.shortcuts import render


# Create your views here.
def register(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def logout(request):
    return render(request,'login.html')

def home(request):
    return render(request,'home.html')

def checklogin(request):
    return render(request,'home.html')

def registerdetails(request):
    firstname= request.GET['first_name']
    return render(request,'home.html',{'firstname':firstname})