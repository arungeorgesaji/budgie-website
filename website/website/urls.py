from django.contrib import *
from django.urls import path,include

urlpatterns =[
    path('admin/', admin.site.urls),
    path('',  include('budgie_website.urls')),
]