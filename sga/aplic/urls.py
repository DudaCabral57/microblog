from django.urls import path

from .views import IndexView, TesteView, ContatoView, SobreView
from rest_framework.routers import SimpleRouter


router = SimpleRouter()



router.register(r'postagens', PostagemViewSet)
router.register(r'comentarios', ComentarioViewSet)
router.register(r'categorias', CategoriaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]