from django import forms

from .models import Postagem, Usuario, Configuracao, Comentario, Categoria, Compartilhamento, Notificacao, Marcacao, Avaliacao, Conteudo, Relato
from django.contrib.auth.models import User


class CustomUserCreationForm(Usuario):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'is_staff')


class CustomUserChangeForm(Usuario):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')


class PostagemForm(forms.ModelForm):
    class Meta:
        model = Postagem
        fields = ['titulo', 'conteudo', 'imagem']


class ConteudoForm(forms.ModelForm):
    class Meta:
        model = Conteudo
        fields = ['titulo', 'descricao', 'imagem', 'categorias']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4, 'cols': 20}),
        }


class AvaliacaoForm(forms.ModelForm):

    class Meta:
        model = Avaliacao

        NOTA_CHOICES = [
            (1, 'Like'),
            (-1, 'Dislike'),
        ]

        nota = forms.ChoiceField(choices=NOTA_CHOICES, widget=forms.RadioSelect)


class RelatoForm(forms.ModelForm):
    class Meta:
        model = Relato
        fields = ['motivo']
        widgets = {
            'motivo': forms.Textarea(attrs={'rows': 4, 'cols': 20}),
        }


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'descricao']