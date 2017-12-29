from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.conf import settings
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Notice


# Create your views here.
@login_required(redirect_field_name='my_redirect_field')
def logout_view(request):
    logout_view(request)


def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, "registration/index.html")


def notice_list(request):
    data = Notice.objects.all()
    context = {
        'data': data
    }
    return render(request, "registration/notice/notice-list.html", context=context)


def create_notice(request):
    if request.method == "GET":
        return render(request, "registration/notice/create-notice.html")
    elif request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        status = request.POST['status']
        data = Notice(title=title, description=description, status=status)
        data.save()
        messages.add_message(request, messages.SUCCESS, 'Success Your data insert successfully!!')
        return redirect('notice_list')
