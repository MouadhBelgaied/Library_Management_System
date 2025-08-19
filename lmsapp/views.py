from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
from django.db.models import Sum

# Create your views here.
def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        
    return render(request, "pages/login.html")

def logout_user(request):
    logout(request)
    return redirect("login_user")

def index(request):
    if not request.user.is_authenticated:
        return redirect("login_user")
    
    if request.POST :
        add_book= BookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()

        add_category= CategoryForm(request.POST, request.FILES)
        if add_category.is_valid():
            add_category.save()

    total_sold= (
    Book.objects.filter(state='sold').aggregate(total_price=Sum('price'))['total_price'] or 0
) 
    total_rental=  (
    Book.objects.filter(state='rental').aggregate(total_rental=Sum('total_rental'))['total_rental'] or 0
)
    total = (
    Book.objects.filter(state='sold').aggregate(total_price=Sum('price'))['total_price'] or 0
) + (
    Book.objects.filter(state='rental').aggregate(total_rental=Sum('total_rental'))['total_rental'] or 0
)
    context={
            'books': Book.objects.all(),
            'categories': Category.objects.all(),
            'form': BookForm,
            'form2': CategoryForm,
            'allbooks' : Book.objects.filter(active=True).count(),
            'soldbooks' : Book.objects.filter(state='sold').count(),
            'rentalbooks' : Book.objects.filter(state='rental').count(),
            'availablebooks' : Book.objects.filter(state='available').count(),
            'total': "{:.3f}".format(total),
            'total_sold':total_sold,
            'total_rental':total_rental,
        }
    return render(request,"pages/index.html",context)

def books (request):
    if not request.user.is_authenticated:
        return redirect("login_user")
    
    if request.POST :
        add_book= BookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()

        add_category= CategoryForm(request.POST, request.FILES)
        if add_category.is_valid():
            add_category.save()

    search=None
    title= None
    context={
            'books': Book.objects.all(),
            'categories': Category.objects.all(),
            'form': BookForm,
            'form2': CategoryForm,
        }
    
    if 'search_name' in request.GET :
        title= request.GET['search_name']
        if title:
            search= Book.objects.filter(title__icontains=title)
            context['books']=search

    return render(request,'pages/books.html',context)

def delete(request,id):
    if not request.user.is_authenticated:
        return redirect("login_user")
    
    book_id = get_object_or_404(Book,id=id)
    if request.method =='POST':
        book_id.delete()
        return redirect('index')

    context={
            'categories': Category.objects.all(),
            'form2': CategoryForm,
        }
    return render(request,'pages/delete.html',context) 

def update(request, id):
    if not request.user.is_authenticated:
        return redirect("login_user")
    
    book_id = Book.objects.get(id=id)
    if request.method == 'POST' :
        update_book= BookForm(request.POST, request.FILES, instance= book_id)
        if update_book.is_valid():
            update_book.save()
            return redirect("index")
    else:
        update_book= BookForm(instance= book_id)

    context={
        'form': update_book,
        'categories': Category.objects.all(),
        'form2': CategoryForm,
    }
    return render(request,'pages/update.html',context) 
    


