from django.urls import path
from .views import PostagemListView, PostagemDetailView, PostagemCreateView, PostagemUpdateView, PostagemDeleteView
from rest_framework.routers import SimpleRouter
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
router = SimpleRouter()

urlpatterns = [
    path('', views.lista_usuarios, name='lista_usuarios'),
    path('novo/', views.criar_usuario, name='criar_usuario'),
    path('<int:pk>/', views.detalhes_usuario, name='detalhes_usuario'),
    path('<int:pk>/editar/', views.editar_usuario, name='editar_usuario'),
    path('<int:pk>/deletar/', views.deletar_usuario, name='deletar_usuario'),
    path('', views.lista_marcacoes, name='lista_marcacoes'),
    path('novo/', views.criar_marcacao, name='criar_marcacao'),
    path('<int:pk>/', views.detalhes_marcacao, name='detalhes_marcacao'),
    path('<int:pk>/editar/', views.editar_marcacao, name='editar_marcacao'),
    path('<int:pk>/deletar/', views.deletar_marcacao, name='deletar_marcacao'),
    path('<int:pk>/aprovar/', views.aprovar_marcacao, name='aprovar_marcacao'),
    path('', views.lista_compartilhamentos, name='lista_compartilhamentos'),
    path('novo/', views.criar_compartilhamento, name='criar_compartilhamento'),
    path('<int:pk>/', views.detalhes_compartilhamento, name='detalhes_compartilhamento'),
    path('<int:pk>/editar/', views.editar_compartilhamento, name='editar_compartilhamento'),
    path('<int:pk>/deletar/', views.deletar_compartilhamento, name='deletar_compartilhamento'),
    path('', views.lista_avaliacoes, name='lista_avaliacoes'),
    path('novo/', views.criar_avaliacao, name='criar_avaliacao'),
    path('<int:pk>/', views.detalhes_avaliacao, name='detalhes_avaliacao'),
    path('<int:pk>/editar/', views.editar_avaliacao, name='editar_avaliacao'),
    path('<int:pk>/deletar/', views.deletar_avaliacao, name='deletar_avaliacao'),
    path('', views.lista_configuracoes, name='lista_configuracoes'),
    path('novo/', views.criar_configuracao, name='criar_configuracao'),
    path('<int:pk>/', views.detalhes_configuracao, name='detalhes_configuracao'),
    path('<int:pk>/editar/', views.editar_configuracao, name='editar_configuracao'),
    path('<int:pk>/deletar/', views.deletar_configuracao, name='deletar_configuracao'),
    path('', views.lista_notificacoes, name='lista_notificacoes'),
    path('novo/', views.criar_notificacao, name='criar_notificacao'),
    path('<int:pk>/', views.detalhes_notificacao, name='detalhes_notificacao'),
    path('<int:pk>/editar/', views.editar_notificacao, name='editar_notificacao'),
    path('<int:pk>/deletar/', views.deletar_notificacao, name='deletar_notificacao'),
]