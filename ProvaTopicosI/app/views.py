from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import App
from .forms import ProdutoForm
from django.contrib import messages
# Create your views here.

def liste(request):
    apps_list = App.objects.all().order_by('-created_at')#pega a lista toda 
    
    paginator = Paginator(apps_list, 3)

    page = request.GET.get('page')

    apps = paginator.get_page(page)

    return render(request, 'telinhas/list.html', {'apps':apps})

def listeViews(request, id):
    relat = get_object_or_404(App, pk=id)#pega apenas um da lista 
    return render(request, 'telinhas/relat.html', {'relat':relat})

def novoProduto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)

        if form.is_valid():
            relat = form.save(commit=False)
            relat.done = 'disponivel'
            relat.save()
            return redirect('/')
    else:    
        form = ProdutoForm()
        return render(request, 'telinhas/addProduto.html', {'form':form})
#ok

def editProduto(request, id):
    relat = get_object_or_404(App, pk=id)
    form = ProdutoForm(instance=relat)

    if request.method =='POST':
        form = ProdutoForm(request.POST, instance=relat)
        if form.is_valid():
            relat.save()
            return redirect('/')
        else:
           return render(request, 'telinhas/editProduto.html', {'form':form, 'relat':relat}) 
    else:
        return render(request, 'telinhas/editProduto.html', {'form':form, 'relat':relat})
#ok
def deleteProduto(request, id):
    relat = get_object_or_404(App, pk=id)
    relat.delete()

    messages.info(request, 'Produto deletado com sucesso!')
    return redirect('/')