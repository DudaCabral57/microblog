from django import forms

from .models import Postagem, Usuario, Configuracao, Comentario, Categoria, Compartilhamento, Notificacao, Marcacao, Avaliacao, Conteudo, Relato
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Usuario  # Isso se refere ao modelo de usuário que você criou
        fields = ('email', 'first_name', 'last_name')  # Ajuste os campos de acordo com o seu modelo

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ('email', 'first_name', 'last_name')  # Ajuste os campos de acordo com o seu modelo

class PostagemForm(forms.ModelForm):
    class Meta:
        model = Postagem  # Supondo que haja um modelo Postagem
        fields = '__all__'


class ConteudoForm(forms.ModelForm):
    class Meta:
        model = Conteudo
        fields = ['titulo', 'descricao', 'categorias', 'imagem']


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