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

def login(request):
    return render(request, "budgie_website/login.html", {})

def lost_password(request):
    return render(request, "budgie_website/lost_password.html", {})

def new_password(request):
    return render(request, "budgie_website/new_password.html", {})

def otp(request):
    return render(request, "budgie_website/otp.html", {})

def sign_in(request):
    return render(request, "budgie_website/sign_in.html", {})   