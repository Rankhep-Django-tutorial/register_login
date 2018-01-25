from django.shortcuts import render, redirect
from django.utils import timezone
from django.db import connection
from .forms import UserDataForm
from .models import UserData


# Create your views here.

def index(request):
    return render(request, 'login/index.html', {})


def register(request):
    if request.method == "POST":
        form = UserDataForm(request.POST)
        qs = UserData.objects.all()
        body = request.POST.get("user_id", "")
        if qs.filter(user_id__contains=body):
            return redirect('register')
        if form.is_valid():
            user_data = form.save(commit=False)
            user_data.published_date = timezone.now()
            user_data.save()
            return redirect('index')
    else:
        form = UserDataForm
    return render(request, 'login/register.html', {'form': form})

# if request.method == "POST":
#        form = PostForm(request.POST)
#        if form.is_valid():
#            post = form.save(commit=False)
#            post.author = request.user
#            post.published_date = timezone.now()
#            post.save()
#            return redirect('post_detail', pk=post.pk)
#    else:
#        form = PostForm()
#    return render(request, 'blog/post_edit.html', {'form': form})
