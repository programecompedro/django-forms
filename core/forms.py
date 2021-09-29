from django import forms
from django.core.mail.message import EmailMessage
from .models import Produto

class ContatoForm(forms.Form):
    nome = forms.CharField(label="Nome", max_length=100)
    email = forms.EmailField(label="Email", max_length=100)
    assunto = forms.CharField(label="Assunto", max_length=120)
    mensagem = forms.CharField(label="Mensagem", widget=forms.Textarea)

    def send_email(self):
        """
        Função que envia E-mail
        """
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'

        mail = EmailMessage(
            subject='E-mail enviado pelo sistema de formulários Django',
            body=conteudo,
            from_email='contato@seudominio.com.br',
            to=['contato@seudominio.com.br'],
            headers={'Reply-To': email}
        )

        mail.send()

class ProdutoForm(forms.ModelForm):
    
    class Meta:
        model = Produto
        fields = ("nome", "preco", "estoque", "imagem")
