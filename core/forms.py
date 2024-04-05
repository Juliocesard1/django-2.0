
from email.message import EmailMessage
from django import forms
from .models import Produto 


class ContatoForm(forms.Form):
    nome = forms.CharField(label='nome')
    email = forms.EmailField(label="e-mail")
    assunto = forms.CharField(label="assunto", max_length=200)
    mensagem = forms.CharField(label="Mesagen", widget=forms.Textarea())



    def send_email(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\nE-mail: {email}\nAsunto: {assunto}\nMensagem:  {mensagem}'

        mail = EmailMessage(
            subject = 'E-mail enviado  pelo sistema django2',
            boddy=conteudo,
            from_email='contato@seudominio.com.br',
            to=['contato@seudominio.com.br'],
            headers={'Reply-To': email}             
        )
        mail.send()
class ProdutoModelForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = ['nome', 'preco','estoque','imagem']

