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
    path('', views.base, name="base"),
]

urlpatterns += staticfiles_urlpatterns()