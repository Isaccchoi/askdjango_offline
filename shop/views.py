from django.shortcuts import redirect, render, get_object_or_404
from .models import Item
from .forms import ItemForm

def item_list(request):
    item_list = Item.objects.all()
    return render(request, 'shop/item_list.html', {'item_list': item_list, })

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'shop/item_detail.html', {'item': item, })

def item_new(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            return redirect(item)
    else:
        form = ItemForm()

    return render(request, 'shop/item_form.html', {'form': form, })

def item_edit(request, pk):
    item = get_object_or_404(Item, pk=pk)

    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            return redirect(item)
    else:
        form = ItemForm(instance=item)
    return render(request, 'shop/item_form.html', {'form': form, })

def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('shop:item_list')
    return render(request, 'shop/item_confirm_delete.html', {'item': item, })