from django.shortcuts import redirect, render
from lists.models import Item,List
from django.core.exceptions import ValidationError

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
    error = None

    if request.method == 'POST':
        try:
            item = Item(text=request.POST['item_text'], list=list_)
            item.full_clean()
            item.save()
            return redirect(list_)
        except ValidationError:
            error = "You can't have an empty list item"

    return render(request, 'list.html', {'list': list_, 'error': error})


def new_list(request):
    list_ = List.objects.create()
    item = Item(text=request.POST['item_text'], list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = "You can't have an empty list item"
        return render(request, 'home.html', {"error": error})
    return redirect(list_)

