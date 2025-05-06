from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import Itemform

# Create your views here.
def item_read(request):
    itens = Item.objects.all()
    return render(request, 'item_read.html', {'itens' : itens})

def item_create(request):
    if request.method == 'POST':
        form = Itemform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_read')
    else:
        form = Itemform()
    return render(request, 'itens_form.html', {'form' : form})

def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = Itemform(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_read')
    else: 
        form = Itemform(instance=item)
    return render(request, 'itens_form.html', {'form' : form})

def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_read')
    return render(request, 'confirmar_delete.html', {'item' : item})