from django.core.mail import message
from django.shortcuts import render
from .forms import ContatoForm, ProdutoForm
from django.contrib import messages
# Create your views here.
def index(request):
    template='index.html'
    return render(request, template)

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

    if request.method == "POST":
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            prod = form.save(commit=False)
            print(f'Nome: {prod.nome}')
            print(f'preco: {prod.preco}')
            print(f'estoque: {prod.estoque}')
            print(f'imagem: {prod.imagem}')
            messages.success(request, 'Formulário salvo com sucesso.')
            form = ProdutoForm()
        else:
            messages.error(request, 'Erro ao salvar produto')
    else:
        form = ProdutoForm()

    context = {
        "form": form
    }
    return render(request, template, context)