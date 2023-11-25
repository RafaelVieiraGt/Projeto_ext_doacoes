from .forms import ProdutoForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from.models import Produto


def registerdoacao(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, 'E-mail enviado com sucesso! ')
            return redirect('registerdoacao')
    else:
        form = ProdutoForm()

    return render(request, 'registerdoacao.html', {'form': form})


def home(request):
    return render(request, 'index.html')

def creditos(request):
    return render(request, 'creditos.html')

def doacoes(request):
    produtos = Produto.objects.all()
    return  render(request, 'doacoes.html', {'produtos': produtos})

def excluir_prod(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    produto.delete()
    return(redirect('doacoes'))


def filter_prod(request):
    categoria = request.GET.get('categoria')



    if categoria:
        produtos = Produto.objects.filter(categoria=categoria)

    if (categoria == "tudo"):
        produtos = Produto.objects.all()

    return render(request, 'doacoes.html', {'produtos': produtos})
