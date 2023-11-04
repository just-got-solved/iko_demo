# produtos/views.py
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from urllib.parse import urlencode
from .forms.forms import PesquisaProdutoForm, IncluirProduto
from .models import Produto, ProdutoConcorrenteFag, ProdutoConcorrenteIna, ProdutoConcorrenteSkf, ProdutoConcorrenteTorrington

def lista_produtos(request):
    query_param = None
    if request.method == 'POST':
        form = PesquisaProdutoForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data.get('product_search_input', '').upper()
            get_return = Produto.objects.filter(
                Q(produto_ina__name=query) |
                Q(produto_skf__name=query) |
                Q(produto_fag__name=query) |
                Q(produto_torrington__name=query)
            )
        else:
            get_return = []
    else:
        form = PesquisaProdutoForm()
        get_return = []
        return get_object_or_404(get_return)

    return render(request, 'produtos/lista_produtos.html', {'produtos': get_return, 'form': form})


def add_produto(request):
    if request.method == 'POST':
        form = IncluirProduto(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['product_nome_input']
            descricao = form.cleaned_data['product_descricao_input']
            preco = form.cleaned_data['product_preco_input']
            print(nome, descricao, preco)
    
    return render(request, 'produtos/add_produtos.html')



def pesquisa(request):
    resultados = None
    if request.method == 'POST':
        form = PesquisaProdutoForm(request.POST)
        
        if form.is_valid():
            query_params = urlencode(form.cleaned_data['product_search_input'].upper())
            if query_params:
                return redirect(lista_produtos)
    else:
        form = PesquisaProdutoForm()

    return render(request, 'produtos/pesquisa.html', {'resultados': resultados, 'form': form})


