from django.shortcuts import render

def base(request):
    return render(request, "budgie_website/base.html", {})

def profile(request):
    return render(request, "budgie_website/profile.html", {})

def about(request):
    return render(request, "budgie_website/about.html", {})

def store(request):
    return render(request, "budgie_website/store.html", {})

def media(request):
    return render(request, "budgie_website/media.html", {})

def guide(request):
    return render(request, "budgie_website/guide.html", {})

def merch(request):
    return render(request, "budgie_website/merch.html", {})