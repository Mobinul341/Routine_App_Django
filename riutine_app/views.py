from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        if form.is_valid:
            form.save()
            all_items = List.objects.all
            messages.success(request, ("Your Schedule has been posted"))
            context = {'title':'Index', 'content':'Routine Index', 'all_items':all_items}
            return render(request, 'index.html', context)
        

    else:
        all_items = List.objects.all
        context = {'title': 'Index',
                    'content': 'Routine Index',
                    'all_items': all_items}
        return render(request, 'index.html', context)

def about(request):
    context = {'title': 'About',
                'content': 'About Us'}
    return render(request, 'about.html', context)


def delete(request, list_id):
    item = List.objects.get(pk = list_id)
    item.delete()
    messages.success(request, ("Schedule has been deleted from List"))
    return redirect('index')


def check_in(request, list_id):
    item = List.objects.get(pk = list_id)
    item.completed = True
    item.save()
    return redirect('index')

def check_out(request, list_id):
    item = List.objects.get(pk = list_id)
    item.completed = False
    item.save()
    return redirect('index')

def edit(request, list_id):
    if request.method == 'POST':
        all_items = List.objects.get(pk = list_id)
        form = ListForm(request.POST or None, instance= all_items)
        if form.is_valid:
            form.save()
            
            messages.success(request, ("Schedule edited"))
            context = {'title':'Edit', 'content':'Edit Page', 'all_items':all_items}
            return redirect('index')
        

    else:
        all_items = List.objects.get(pk=list_id)
        context = {'title': 'Edit',
                    'content': 'Routine Index',
                    'all_items': all_items}
        return render(request, 'edit.html', context)



