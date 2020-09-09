from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name='beranda'),
    path('about/',views.about, name='about'),
    path('login/',views.login, name='login'),
    path('result/',views.result, name='result'),
]