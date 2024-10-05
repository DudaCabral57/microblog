from django.contrib import admin

from .models import Usuario, Configuracao, Comentario, Categoria, Compartilhamento, Avaliacao, Postagem, Notificacao, Marcacao


@admin.register(Usuario)
class UserAdmin(admin.ModelAdmin):
    list_display = ('@')
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'titulacao')

@admin.register(Configuracao)
class ConfiguracaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'curso')

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'carga_horaria')

@admin.register(Compartilhamento)
class CompartilhamentoAdmin(admin.ModelAdmin):
    list_display = ('ano', 'semestre', 'disciplina')
@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'disciplina', 'carga_horaria')
@admin.register(Postagem)
class PostagemAdmin(admin.ModelAdmin):
    list_display = ('nome', 'disciplina', 'carga_horaria')
@admin.register(Marcacao)
class MarcacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'disciplina', 'carga_horaria')
@admin.register(Notificacao)
class NotificacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'disciplina', 'carga_horaria')
