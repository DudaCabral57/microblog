import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Usuario(models.Model):
    nome = models.CharField('Nome: ', max_length=60)
    email = models.EmailField('Email: ', max_length=254)
    senha = models.CharField('Senha: ', max_length=50)
    telefone = models.CharField('Telefone: ', max_length=11)
    username = models.CharField('Nome de usuário: ', max_length=20)
    bio = models.TextField('Digite sua bio: ', max_length=250)
    foto_perfil = models.ImageField('Foto de Perfil: ', upload_to=get_file_path, null=True, blank=True)
    seguidores = models.ManyToManyField('self', blank=True, related_name='seguidores')
    seguindo = models.ManyToManyField('self', blank=True, related_name='seguindo')

    def __str__(self):
        return self.username

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
    preferencias = models.CharField('Preferencias: ', max_length=50)
    notificacao = models.BooleanField(default=True)
    bloqueados = models.TextField(blank=True, null=True)
    silenciados = models.TextField(blank=True, null=True)

class Notificacao(models.Model):
    conteudo_notif = models.TextField()
    data_recebimento = models.DateTimeField(auto_now_add=True)

class Avaliacao(models.Model):
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_aval = models.DateTimeField(auto_now_add=True)
    perfil_aval = models.CharField(max_length=100)
    positiva_negativa = models.BooleanField()
    reportar_post = models.CharField(max_length=100)
    contador_aval_positiva = models.IntegerField(default=0)
    contador_aval_negativa = models.IntegerField(default=0)

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Comentario(models.Model):
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    conteudo = models.TextField(max_length=250)
    data_criacao = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to=get_file_path, null=True, blank=True)

class Postagem(models.Model):
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50, null=True, blank=True)
    conteudo = models.TextField(max_length=250)
    data_criacao = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    slug = models.SlugField(unique=True, max_length=50)

    def __str__(self):
        return f"Postagem de {self.autor.username}: {self.titulo}"

class Compartilhamento(models.Model):
    post_republicado = models.ForeignKey(Postagem, on_delete=models.CASCADE)
    perfil_postando = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="perfil_postando")
    perfil_republicado = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="perfil_republicado")
    data_repost = models.DateTimeField(auto_now_add=True)
    contador_compartilhamento = models.IntegerField(default=0)

class Marcacao(models.Model):
    perfil_marcado = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="perfil_marcado")
    perfil_marcando = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="perfil_marcando")
    aprovacao = models.BooleanField()
