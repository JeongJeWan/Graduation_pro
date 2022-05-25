from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from videoapp.forms import Video_form
from videoapp.models import Video


def index(request):
    all_video = Video.objects.all()
    if request.method == "POST":
        form = Video_form(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('videoapp:list')
    else:
        form = Video_form()
    return render(request, 'videoapp/index.html', {"form": form, "all": all_video})


def list_index(request):
    all_video = Video.objects.all()
    if request.method == "POST":
        form = Video_form(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('videoapp:list')
    else:
        form = Video_form()
    return render(request, 'videoapp/list.html', {"form": form, "all": all_video})
