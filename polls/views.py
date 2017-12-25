from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Book

# Create your views here.
def hi(request):
    return HttpResponse("bye")


def index(request):
    if request.method == 'GET':
        return render(request, "html/index.html")
    elif request.method == 'POST':
        title =  request.POST.get('title',"" )
        description = request.POST.get('description',"")
        b = Book(title=title,description=description)
        b.save()
        context ={
            'title': title,
            'description': description,
        }
        # print("::::::::---- this wase title '%s' des is %s " % (name,description) )
        return render(request, "html/index.html",context= context)


def about(r):
    return render(r, "html/about.html")


def reyad(r):
    return HttpResponse("heello reyad")


def list(request):
    book = Book.objects.all()
    context={
        'book':book
    }
    return render(request,"html/list.html",context= context)
# def saveItem(request):
#     name = status = request.GET('status')
#     return HttpResponse("save done")