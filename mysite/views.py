from django.shortcuts import render, redirect
from django.utils import timezone
from django.db import connection
from .forms import UserDataForm
from .models import UserData


# Create your views here.

def index(request):
    if request.method == "POST":
        form = UserDataForm(request.POST)
        qs = UserData.objects.all()
        id_check = request.POST.get("user_id", "")
        pwd_check = request.POST.get("user_pwd", "")
        print(id_check, '+', pwd_check)
        if qs.filter(user_id=id_check, user_pwd=pwd_check):
            print('complete.html')
            return redirect('complete')
        else:
            print('fail')
            return redirect('index')
    else:
        form = UserDataForm
    return render(request, 'login/index.html', {})


def register(request):
    if request.method == "POST":
        form = UserDataForm(request.POST)
        qs = UserData.objects.all()
        body = request.POST.get("user_id", "")
        if qs.filter(user_id=body):
            return redirect('register')
        if form.is_valid():
            user_data = form.save(commit=False)
            user_data.published_date = timezone.now()
            user_data.save()
            return redirect('index')
    else:
        form = UserDataForm
    return render(request, 'login/register.html', {'form': form})


def complete(request):
    return render(request, 'login/complete.html')
