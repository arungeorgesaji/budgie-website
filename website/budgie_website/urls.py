from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

urlpatterns =[
    path('profile/', views.profile, name="profile"),
    path('about/', views.about, name="about"),
    path('store/', views.store, name="store"),
    path('media/', views.media, name="media"),
    path('guide/', views.guide, name="guide"),
    path('merch/', views.merch, name="merch"),
    path('login/', views.login, name="login"),
    path('', views.base, name="base"),
    path('lost_password/', views.lost_password, name="lost_password"),
    path('new_password/', views.new_password, name="new_password"),
    path('otp/', views.otp, name="otp"),
    path('sign_in/', views.sign_in, name="sign_in"),
]

urlpatterns += staticfiles_urlpatterns()