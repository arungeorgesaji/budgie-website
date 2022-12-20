from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
import smtplib
from django.contrib import messages
from email.message import EmailMessage

def base(request):
    return render(request, "budgie_website/base.html")

def profile(request):
    return render(request, "budgie_website/profile.html")

def about(request):
    return render(request, "budgie_website/about.html")

def store(request):
    return render(request, "budgie_website/store.html")

def media(request):
    return render(request, "budgie_website/media.html")

def guide(request):
    return render(request, "budgie_website/guide.html")

def merch(request):
    return render(request, "budgie_website/merch.html")

def sign_in(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('http://127.0.0.1:8000/profile/')

        else:
            messages.error(request, "Bad Credentials")
            return redirect('http://127.0.0.1:8000/login/')
             
    return render(request, "budgie_website/login.html")

def lost_password(request):
    return render(request, "budgie_website/lost_password.html",)

def new_password(request):
    return render(request, "budgie_website/new_password.html")

def otp(request):
    return render(request, "budgie_website/otp.html")

def register(request):

    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        if User.objects.filter(username = username).first():
            messages.error(request, "Username not available")
            return redirect('http://127.0.0.1:8000/sign_in/') 
        else:
            user = User.objects.create_user(username,email, password)
            user.save()

            message = EmailMessage()
            content = "Welcome to budgie world the everything budgie website it contains budgie guides,budgie media.It also allows you to buy budgie merch and actual budgies.We are also happy to announce that we are working on a budgie 3d game and we are also working on a app which will allow you to record budgie sound and it will convert it into english text for you to understand.We are working day and night to complete and release these,I hope you enjoy our services budgie services"
            message.set_content(content)
            message['From'] = "arungeorgesaji@gmail.com"
            message['To'] = email
            message['Subject'] = "You have sucessfully registered to budgie world the everything budgie website"
            
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login("arungeorgesaji@gmail.com", "xunmcovoyaeuahwi")
            server.send_message(message)
            server.quit()
            
            return redirect('http://127.0.0.1:8000/login/') 
        
            
    return render(request,"budgie_website/sign_in.html")
