from django import forms

class PesquisaProdutoForm(forms.Form):
    product_search_input = forms.CharField(
        label='Pesquisar produtos', 
        max_length=100, 
        widget=forms.TextInput(attrs={'placeholder': 'Digite o produto desejado'})
    )


class IncluirProduto(forms.Form):
    product_nome_input = forms.CharField(
        label='Nome', 
        max_length=100, 
        widget=forms.TextInput(attrs={'placeholder': 'Nome'})
    )
    product_descricao_input = forms.CharField(
        label='descricao', 
        max_length=200, 
        widget=forms.TextInput(attrs={'placeholder': 'Descrição'})
    )
    product_preco_input = forms.CharField(
        label='preco', 
        widget=forms.NumberInput(attrs={'placeholder': 'Preço'})
    )
   