from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Postagem
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Postagem
from .forms import PostagemForm

# Lista de postagens (Read - Lista)
class PostagemListView(ListView):
    model = Postagem
    template_name = 'aplic/postagem_list.html'
    context_object_name = 'postagens'

# Detalhes de uma postagem (Read - Detalhes)
class PostagemDetailView(DetailView):
    model = Postagem
    template_name = 'aplic/postagem_detail.html'
    context_object_name = 'postagem'

# Criação de nova postagem (Create)
class PostagemCreateView(CreateView):
    model = Postagem
    form_class = PostagemForm
    template_name = 'aplic/postagem_form.html'
    success_url = reverse_lazy('postagem-list')

# Atualização de uma postagem (Update)
class PostagemUpdateView(UpdateView):
    model = Postagem
    form_class = PostagemForm
    template_name = 'aplic/postagem_form.html'
    success_url = reverse_lazy('postagem-list')

# Deleção de uma postagem (Delete)
class PostagemDeleteView(DeleteView):
    model = Postagem
    template_name = 'aplic/postagem_confirm_delete.html'
    success_url = reverse_lazy('postagem-list')


# Lista de postagens (Read - Lista)
class PostagemListView(ListView):
    model = Postagem
    template_name = 'aplic/postagem_list.html'
    context_object_name = 'postagens'

# Detalhes de uma postagem (Read - Detalhes)
class PostagemDetailView(DetailView):
    model = Postagem
    template_name = 'aplic/postagem_detail.html'
    context_object_name = 'postagem'

# Criação de nova postagem (Create)
class PostagemCreateView(CreateView):
    model = Postagem
    form_class = PostagemForm
    template_name = 'aplic/postagem_form.html'
    success_url = reverse_lazy('postagem-list')

# Atualização de uma postagem (Update)
class PostagemUpdateView(UpdateView):
    model = Postagem
    form_class = PostagemForm
    template_name = 'aplic/postagem_form.html'
    success_url = reverse_lazy('postagem-list')

# Deleção de uma postagem (Delete)
class PostagemDeleteView(DeleteView):
    model = Postagem
    template_name = 'aplic/postagem_confirm_delete.html'
    success_url = reverse_lazy('postagem-list')




class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context


class TesteView(TemplateView):
    template_name = 'teste.html'

    def get_context_data(self, **kwargs):
        context = super(TesteView, self).get_context_data(**kwargs)
        return context


class SobreView(TemplateView):
    template_name = 'sobre.html'

    def get_context_data(self, **kwargs):
        context = super(SobreView, self).get_context_data(**kwargs)
        return context


class ContatoView(TemplateView):
    template_name = 'contato.html'

    def get_context_data(self, **kwargs):
        context = super(ContatoView, self).get_context_data(**kwargs)
        return context

