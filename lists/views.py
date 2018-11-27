from django.shortcuts import redirect, render
from lists.models import Item


def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/the-only-list-in-the-world/')

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


def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})
