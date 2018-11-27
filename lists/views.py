from django.shortcuts import redirect, render
from lists.models import Item,List


def home_page(request):
    return render(request, 'home.html')


"""
from django.shortcuts import render
from lists.models import Item

def home_page(request):
    if request.method == 'POST':
        new_item_text = request.POST['item_text'] #1
        Item.objects.create(text=new_item_text) #2
    else:
        new_item_text = '' #1

    return render(request, 'home.html', {
        'new_item_text': new_item_text, #1
    })

#1 We use a variable called new_item_text, which will either hold the POST contents, or the empty string.
#2 .objects.create is a neat shorthand for creating a new Item, without needing to call .save().


"""


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': list_})


def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')


def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')