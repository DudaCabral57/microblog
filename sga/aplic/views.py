from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

f

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Postagem, Avaliacao, Usuario, Configuracao, Comentario, Categoria, Compartilhamento, Marcacao, Notificacao, Conteudo
from .forms import PostagemForm, CustomUserCreationForm, CustomUserChangeForm, RelatoForm, AvaliacaoForm, ConteudoForm, CategoriaForm


class PostagemListView(ListView):
    model = Postagem
    template_name = 'aplic/postagem_list.html'
    context_object_name = 'postagens'


class PostagemDetailView(DetailView):
    model = Postagem
    template_name = 'aplic/postagem_detail.html'
    context_object_name = 'postagem'


class PostagemCreateView(CreateView):
    model = Postagem
    form_class = PostagemForm
    template_name = 'aplic/postagem_form.html'
    success_url = reverse_lazy('postagem-list')


class PostagemUpdateView(UpdateView):
    model = Postagem
    form_class = PostagemForm
    template_name = 'aplic/postagem_form.html'
    success_url = reverse_lazy('postagem-list')


class PostagemDeleteView(DeleteView):
    model = Postagem
    template_name = 'aplic/postagem_confirm_delete.html'
    success_url = reverse_lazy('postagem-list')


def listar_conteudos(request):
    conteudos = Conteudo.objects.all()
    return render(request, 'listar_conteudos.html', {'conteudos': conteudos})


def detalhe_conteudo(request, conteudo_id):
    conteudo = get_object_or_404(Conteudo, id=conteudo_id)
    avaliacao_form = AvaliacaoForm()
    relato_form = RelatoForm()
    return render(request, 'detalhe_conteudo.html', {
        'conteudo': conteudo,
        'avaliacao_form': avaliacao_form,
        'relato_form': relato_form,
    })

o
def criar_conteudo(request):
    if request.method == 'POST':
        form = ConteudoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_conteudos')
    else:
        form = ConteudoForm()
    return render(request, 'criar_conteudo.html', {'form': form})

# Atualizar um conteúdo existente
def atualizar_conteudo(request, conteudo_id):
    conteudo = get_object_or_404(Conteudo, id=conteudo_id)
    if request.method == 'POST':
        form = ConteudoForm(request.POST, instance=conteudo)
        if form.is_valid():
            form.save()
            return redirect('detalhe_conteudo', conteudo_id=conteudo.id)
    else:
        form = ConteudoForm(instance=conteudo)
    return render(request, 'atualizar_conteudo.html', {'form': form})


def deletar_conteudo(request, conteudo_id):
    conteudo = get_object_or_404(Conteudo, id=conteudo_id)
    if request.method == 'POST':
        conteudo.delete()
        return redirect('listar_conteudos')
    return render(request, 'deletar_conteudo.html', {'conteudo': conteudo})


def reportar_post(request, conteudo_id):
    conteudo = get_object_or_404(Conteudo, id=conteudo_id)
    if request.method == 'POST':
        form = RelatoForm(request.POST)
        if form.is_valid():
            relato = form.save(commit=False)
            relato.usuario = request.user
            relato.conteudo = conteudo
            relato.save()
            return redirect('detalhe_conteudo', conteudo_id=conteudo.id)
    else:
        form = RelatoForm(initial={'conteudo': conteudo})
    return render(request, 'reportar_post.html', {'form': form, 'conteudo': conteudo})

# Listar todos os relatos
def listar_relatos(request):
    relatos = Relato.objects.all()
    return render(request, 'listar_relatos.html', {'relatos': relatos})
def criar_avaliacao(request, conteudo_id):
    conteudo = get_object_or_404(Conteudo, id=conteudo_id)
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            avaliacao = form.save(commit=False)
            avaliacao.usuario = request.user
            avaliacao.conteudo = conteudo
            avaliacao.save()
            return redirect('detalhe_conteudo', conteudo_id=conteudo.id)
    else:
        form = AvaliacaoForm()
    return render(request, 'criar_avaliacao.html', {'form': form, 'conteudo': conteudo})


def listar_avaliacoes(request, conteudo_id):
    conteudo = get_object_or_404(Conteudo, id=conteudo_id)
    avaliacoes = Avaliacao.objects.filter(conteudo=conteudo)
    return render(request, 'listar_avaliacoes.html', {'conteudo': conteudo, 'avaliacoes': avaliacoes})


def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'listar_categorias.html', {'categorias': categorias})

# Criar nova categoria
def criar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'criar_categoria.html', {'form': form})


def detalhe_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    conteudos = categoria.conteudos.all()
    return render(request, 'detalhe_categoria.html', {'categoria': categoria, 'conteudos': conteudos})


def atualizar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('detalhe_categoria', categoria_id=categoria.id)
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'atualizar_categoria.html', {'form': form})


def deletar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('listar_categorias')
    return render(request, 'deletar_categoria.html', {'categoria': categoria})