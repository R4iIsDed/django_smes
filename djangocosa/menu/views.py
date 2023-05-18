from django.shortcuts import render

# Create your views here.
def login (request) :
    return render(request, 'menu/login.html');

def create (request) :
    return render (request, 'menu/create.html');

def index (request) :
    return render (request, 'menu/index.html');