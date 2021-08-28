from django.shortcuts import render

# Create your views here.


def index(request):
    pass 

def add(request):
    context = {}

    html = 'pengguna/add.html'
    return render (request, html,context) 

def edit(request):
    pass 

def save(request):
    pass 

def delete(request, id):
    pass 