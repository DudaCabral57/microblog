import uuid
from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from django.utils.translation import gettext_lazy as _




def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Usuario(AbstractBaseUser,BaseUserManager, PermissionsMixin):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    senha = models.CharField('Senha: ', max_length=50)
    telefone = models.CharField('Telefone: ', max_length=11)
    username = models.CharField('Nome de usuário: ', max_length=20)
    bio = models.TextField('Digite sua bio: ', max_length=250)
    foto_perfil = models.ImageField('Foto de Perfil: ', upload_to=get_file_path, null=True, blank=True)
    seguidores = models.ManyToManyField('self', blank=True, related_name='seguidores')
    seguindo = models.ManyToManyField('self', blank=True, related_name='seguindo')

    USERNAME_FIELD = ['Username']
    REQUIRED_FIELDS = ['nome']

    def __str__(self):
        return self.username

    def __innit__(self, nome, email):
        self.nome = nome
        self.email = email


def exibir_dados(self):
    return f"Nome: {self.nome}, Email: {self.email}"


class Meta:
    verbose_name = 'Usuário'
    verbose_name_plural = 'Usuários'


class UsuarioManager(BaseUserManager):
    def create_user(self, email, nome, password=None):
        if not email:
            raise ValueError('O campo email é obrigatório.')

        email = self.normalize_email(email)
        user = self.model(email=email, nome=nome)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nome, password=None):
        user = self.create_user(email, nome, password)
        user.is_admin = True
        user.save(using=self._db)
        return user


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
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    mensagem = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    lida = models.BooleanField(default=False)

    def __str__(self):
        return f"Notificação para {self.usuario.username}: {self.mensagem[:20]}..."

    def __innit__(self, usuario_destino, usuario_origem, postagem):
        self.usuario_origem = usuario_origem
        self.usuario_destino = usuario_destino
        self.postagem = postagem


def enviar_notificacao(self):
    return f"Nova notificação para {self.usuario_destino}:" f"{self.usuario_origem} interagiu com sua postagem: '{self.post.conteudo}"


class Avaliacao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='avaliacoes')
    conteudo = models.TextField()  #
    like = models.BooleanField(default=False)
    data_avaliacao = models.DateTimeField(auto_now_add=True)

    @property
    def total_likes(self):
        return self.avaliacao.filter(like=True).count()

    @property
    def total_dislikes(self):
        return self.avaliacao.filter(like=False).count()

    def __str__(self):
        tipo_avaliacao = "Like" if self.like else "Dislike"
        return f'{tipo_avaliacao} de {self.usuario.username} para o conteúdo: {self.conteudo[:20]}...'



class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Conteudo(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    categorias = models.ManyToManyField(Categoria, related_name='conteudos', blank=True)
    imagem = models.ImageField(upload_to='imagens/', blank=True, null=True)

    def __str__(self):
        return self.titulo

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
    post_republicado = models.ForeignKey(Postagem, on_delete=models.CASCADE)
    perfil_postando = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="perfil_postando")
    perfil_republicado = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="perfil_republicado")
    data_repost = models.DateTimeField(auto_now_add=True)
    contador_compartilhamento = models.IntegerField(default=0)


class Marcacao(models.Model):
    perfil_marcado = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="perfil_marcado")
    perfil_marcando = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="perfil_marcando")
    aprovacao = models.BooleanField(default=False)


class Relato(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='relatos')
    conteudo = models.ForeignKey('Conteudo', on_delete=models.CASCADE, related_name='relatos')
    motivo = models.TextField()
    data_relato = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Relato de {self.usuario.username} para o conteúdo: {self.conteudo.titulo}'