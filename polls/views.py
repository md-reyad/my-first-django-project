from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Book
from django.shortcuts import redirect
from django.contrib import messages


# Create your views here.
def hi(request):
    return HttpResponse("bye")


def index(request):
    if request.method == 'GET':
        return render(request, "registration/index.html")
    elif request.method == 'POST':
        title =  request.POST.get('title',"" )
        description = request.POST.get('description',"")
        b = Book(title=title, description=description)
        b.save()
        context ={
            'title': title,
            'description': description,
        }
        # print("::::::::---- this wase title '%s' des is %s " % (name,description) )
        messages.add_message(request, messages.SUCCESS, 'Success Your data insert successfully!!')
        return redirect('list')





def about(r):
    return render(r, "registration/about.registration")


def reyad(r):
    return HttpResponse("heello reyad")


def list(request):
    book = Book.objects.raw('select * from polls_book ORDER  by id DESC ')
    context={
        'book':book
    }
    return render(request,"registration/list.registration",context= context)


def edit(request, id):
    book = Book.objects.get(id=id)
    context={
        'book':book
    }
    return render(request,"registration/edit.registration",context= context)


def update(request, id):
    book = Book.objects.get(id=id)
    book.title=request.POST['title']
    book.description=request.POST['description']
    book.save()
    messages.add_message(request, messages.SUCCESS,"Data Update successfully")
    return redirect('list')
# def saveItem(request):
#     name = status = request.GET('status')
#     return HttpResponse("save done")