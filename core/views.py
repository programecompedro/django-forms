from django.core.mail import message
from django.shortcuts import redirect, render
from .forms import ContatoForm, ProdutoForm
from django.contrib import messages
from .models import Produto


def index(request):
    template='index.html'
    produtos = Produto.objects.all()
    context={
        "produtos":produtos
    }
    return render(request, template, context)

def contato(request):
    template='contato.html'
    form = ContatoForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.send_email()

            messages.success(request, 'E-mail Enviado com sucesso!')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar E-mail')

    context = {
        "form": form
    }
    return render(request, template, context)

def produto(request):
    template='produto.html' 
    if str(request.user) != 'AnonymousUser':
    
        if request.method == "POST":
            form = ProdutoForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()            
                messages.success(request, 'Formulário salvo com sucesso.')
                form = ProdutoForm()
            else:
                messages.error(request, 'Erro ao salvar produto')
        else:
            form = ProdutoForm()
    else:
        return redirect("index")

    context = {
        "form": form
    }
    return render(request, template, context)