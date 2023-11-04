from django.shortcuts import render, redirect
from .models import Contato
from .forms.form_contato import InformacaoContatoForm

def cadastrar_informacao_contato(request):
    if request.method == 'POST':
        form = InformacaoContatoForm(request.POST)
        if form.is_valid():
            new_contato = Contato(
                contato_nome_input = form.cleaned_data['contato_nome_input'],
                contato_email_input = form.cleaned_data['contato_email_input'],
                contato_telefone_input =  form.cleaned_data['contato_telefone_input'],
                contato_empresa_input = form.cleaned_data['contato_empresa_input']
                )
            new_contato.save()
            return render(request, 'contatos/cadastrar_contato.html', {'form': form})
    else:
        form = InformacaoContatoForm()
    
        return render(request, 'contatos/cadastrar_contato.html', {'form': form})
    

def cadastrar_contato(request):
    if request.method == 'POST':
        form = InformacaoContatoForm(request.POST)
        if form.is_valid():
            # salvar_contato(form)
            return redirect(cadastrar_informacao_contato)
        else:
            return render(request, 'contatos/cadastrar_contato.html', {'form': form})
    else:
        form = InformacaoContatoForm()

    return render(request, 'contatos/cadastrar_contato.html', {'form': form})

def salvar_contato(form):
    Contato(
        contato_nome_input = form.cleaned_data['contato_nome_input'],
        contato_email_input = form.cleaned_data['contato_email_input'],
        contato_telefone_input = form.cleaned_data['contato_telefone_input'],
        contato_empresa_input = form.cleaned_data['contato_empresa_input'],
    ).save()

    return 