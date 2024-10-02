import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

# Create your models here.


class usuario(models.Model):
    nome = models.CharField(('Nome: '), max_length=100)
    email = models.CharField(('Email: '), max_length=100)
    senha = models.CharField(('Senha: '), max_length=50)
    telefone = models.CharField (('Telefone: '), max_length=11)
    username = models.CharField (('Nome de usuário: '),max_length=20 )
    bio = models.TextField(('Digite sua bio: '), max_length=500)

class configuracao(models.Model):
    privacidade = models.
    notificacao = models.BooleanField
    bloqueados = models.CharField
    silenciados = models.CharField

class notificacao(models.Model):
    conteudo_notif = models.TextField((''))
    data_recebimento = models.DateTimeField



class avaliacao(models.Model):
    data_aval = models.DateTimeField
    perfil_aval = models.CharField
    positiva_negativa = models.BooleanField
    reportar_post = models.CharField

class categoria(models.Model):
    nome = models.
    def __str__(self):
        return self.nome