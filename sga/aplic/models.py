import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Usuario(models.Model, AbstractUser):
    nome = models.CharField(('Nome: '), max_length=60)
    telefone = models.CharField(('Telefone: '), max_length=11)
    bio = models.TextField(('Digite sua bio: '), max_length=250)
    foto_perfil = models.ImageField(('Selecione sua foto de Perfil: '), upload_to=get_file_path, null=True, blank=True)
    seguidores = models.ManyToManyField('self', blank=True, related_name= 'seguidores')
    seguindo = models.ManyToManyField('self', blank=True, related_name= 'seguindo')


def __innit__(self, nome, email):
    self.nome = nome
    self.email = email


def exibir_dados(self):
    return f"Nome: {self.nome}, Email: {self.email}"


class Meta:
    verbose_name = 'Usuário'
    verbose_name_plural = 'Usuários'


class Configuracao(models.Model):
    PUBLICA = 'publica'
    PRIVADA = 'privada'

    PRIVACIDADE_CHOICES = [
            (PUBLICA, 'Pública'),
            (PRIVADA, 'Privada'),
        ]

    privacidade = models.CharField(
            max_length=7,
            choices=PRIVACIDADE_CHOICES,
            default=PUBLICA
        )


preferencias = models.CharField(('Preferencias: '), max_length=50)
notificacao = models.BooleanField(default=True)
bloqueados = models.CharField
silenciados = models.CharField


class Notificacao(models.Model):
    conteudo_notif = models.TextField('')
    data_recebimento = models.DateTimeField(auto_now_add=True)


    def __innit__(self, usuario_destino, usuario_origem, postagem):
        self.usuario_origem = usuario_origem
        self.usuario_destino = usuario_destino
        self.postagem = postagem


def enviar_notificacao(self):
    return f"Nova notificação para {self.usuario_destino}:" f"{self.usuario_origem} interagiu com sua postagem: '{self.post.conteudo}"


class Avaliacao(models.Model):
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_aval = models.DateTimeField(auto_now_add=True)
    perfil_aval = models.CharField
    positiva_negativa = models.BooleanField
    reportar_post = models.CharField
    contador_aval_positiva = models.IntegerField
    contador_aval_negativa = models.IntegerField


class Categoria(models.Model):
    nome = models.CharField

    def __str__(self):
        return self.nome


class Postagem(models.Model):
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50, null=True, blank=True)
    conteudo = models.TextField(max_length=250)
    data_criacao = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    slug = models.SlugField(unique=True, max_length=50)

    def __str__(self):
        return self.titulo

    def __innit__(self, usuario, conteudo):
        self.autor = usuario
        self.conteudo = conteudo


class Comentario(models.Model):
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    conteudo = models.TextField(max_length=250)
    data_criacao = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    postagem = models.ForeignKey(Postagem, related_name='comentarios', on_delete=models.CASCADE)

    def __str__(self):
        return f'Comentário de {self.autor.username}'


class Compartilhamento(models.Model):
    post_republicado = models.CharField
    perfil_postando = models.CharField
    perfil_republicado = models.CharField
    data_repost = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    contador_compartilhamento = models.IntegerField


class Marcacao(models.Model):
    perfil_marcado = models.CharField
    perfil_marcando = models.CharField
    aprovacacao = models.BooleanField

    def exibir_post(self, usuario, conteudo):
        return f"Post de {self.usuario.username}: {self.conteudo}"