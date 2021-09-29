from django.shortcuts import render

# Create your views here.
def index(request):
    template='index.html'
    return render(request, template)

def contato(request):
    template='contato.html'
    return render(request, template)

def produto(request):
    template='produto.html' 
    return render(request, template)