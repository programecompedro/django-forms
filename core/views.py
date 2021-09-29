from django.shortcuts import render
from .forms import ContatoForm
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
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            print('Mensagem Enviada ')
            print(f'{nome}')
            print(f'{email}')
            print(f'{assunto}')
            print(f'{mensagem}')

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
    return render(request, template)