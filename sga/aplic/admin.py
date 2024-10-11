from django.contrib import admin

from django import forms
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Configuracao, Comentario, Categoria, Compartilhamento, Avaliacao, Postagem, Notificacao, Marcacao, Conteudo, Relato
from .forms import CustomUserCreationForm, CustomUserChangeForm, PostagemForm


class PostagemAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data_criacao')
    list_filter = ('autor', 'data_criacao')
    search_fields = ('titulo', 'conteudo')
    ordering = ('-data_criacao')


@admin.register(Postagem)
class PostagemAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data_criacao')
    list_filter = ('autor', 'data_criacao')
    search_fields = ('titulo', 'conteudo')
    ordering = ('-data_criacao',)


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('postagem', 'autor')
    list_filter = ('autor', )
    search_fields = ('conteudo',)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)


@admin.register(Usuario)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ('Username', 'email', 'first_name', 'last_name',)
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('Username',)


admin.site.unregister(Usuario)
admin.site.register(Usuario, CustomUserAdmin)


class UsuarioInline(admin.StackedInline):
    model = Usuario
    can_delete = False
    verbose_name_plural = 'Perfis'


@admin.register(Configuracao)
class ConfiguracaoAdmin(admin.ModelAdmin):
    list_display = ('PUBLICA', 'PRIVADA', 'preferencias', 'notificacao')


class CompartilhamentoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'postagem', 'data_compartilhamento')
    list_filter = ('data_compartilhamento',)
    search_fields = ('usuario__username', 'postagem__titulo')
    date_hierarchy = 'data_compartilhamento'


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'tipo_avaliacao', 'data_avaliacao', 'conteudo_resumido')
    search_fields = ('usuario__username', 'conteudo')
    list_filter = ('like', 'data_avaliacao')
    date_hierarchy = 'data_avaliacao'

    def tipo_avaliacao(self, obj):
        return "Like" if obj.like else "Dislike"

    tipo_avaliacao.short_description = 'Tipo de Avaliação'

    def conteudo_resumido(self, obj):
        return obj.conteudo[:50] + '...' if len(obj.conteudo) > 50 else obj.conteudo

    conteudo_resumido.short_description = 'Conteúdo Avaliado'



@admin.register(Notificacao)
class NotificacaoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'mensagem_curta', 'data_criacao', 'lida')
    list_filter = ('lida', 'data_criacao')
    search_fields = ('usuario__username', 'mensagem')

    def mensagem_curta(self, obj):
        return obj.mensagem[:40]
    mensagem_curta.short_description = 'Mensagem'



@admin.register(Relato)
class RelatoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'conteudo', 'data_relato', 'motivo')
    search_fields = ('usuario__username', 'conteudo__titulo', 'motivo')
    list_filter = ('data_relato',)
    date_hierarchy = 'data_relato'