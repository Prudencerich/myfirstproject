from django.shortcuts import render

<<<<<<< HEAD
from item.models import Category, Item

from django.forms import SignupForm
=======
>>>>>>> f1ae76f4e1bb0942d0975b8011123ce4072c107d

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html',{
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })