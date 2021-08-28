from django.shortcuts import render

from .forms import PenggunaForm
# Create your views here.

app_name = 'pengguna'

def index(request):
    pass 

def add(request):
    context = {}
    
    context['form'] = PenggunaForm()

    html = 'pengguna/add.html'
    return render (request, html,context) 

def edit(request):
    pass 

def save(request):
    func_name = "save"
    context = {}

    print("THIS IS SAVE FUNC @" + app_name) 
    if request.method == 'POST':
        _POST = request.POST
        try:
            data = Pengguna(request.POST)        
            data.save()
        except Exception as e:
            print ("exce on @" + app_name + "/" + func_name)
            print (e)
        


def delete(request, id):
    pass 