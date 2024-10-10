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

    path('novo/', views.criar_usuario, name='criar_usuario'),
    path('<int:pk>/', views.detalhes_usuario, name='detalhes_usuario'),
    path('novo/', views.criar_conteudo, name='criar_conteudo'),
    path('<int:pk>/aprovar/', views.reportar_post, name='reportar_post'),
    path('', views.listar_avaliacoes, name='lista_avaliacoes'),
    path('novo/', views.criar_avaliacao, name='criar_avaliacao'),

]