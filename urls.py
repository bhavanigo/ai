"""WebC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [ 


    path('', views.homepage, name="WelcomeHome"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('adminloginaction/', views.adminloginaction, name="adminloginaction"),
    path('adminhome/', views.adminhome, name="adminhome"),
    path('userhome/', views.userhome, name="userhome"),
    path('adminlogout/', views.adminlogout, name="adminlogout"),
    path('usignupaction/', views.usignupaction, name="usignupaction"),
    path('user/', views.user, name="user"),
    path('usersignup/', views.usersignup, name="usersignup"),
    path('userloginaction/', views.userloginaction, name="userloginaction"),
    path('userlogout/', views.userlogout, name="userlogout"),
    


    path('training/', views.training, name="training"),
    path('evaluation/', views.evaluation, name="evaluation"),
    path('eval/', views.evaluation, name="eval"),

    path('datasetpage/', views.datasetpage, name="datasetpage"),
    path('upload/', views.upload, name="upload"),


    path('examinit/', views.examinit, name="examinit"),
    path('examstart/', views.examstart, name="examstart"),
    path('answerpro/', views.answerpro, name="answerpro"),
    path('answerpro2/', views.answerpro2, name="answerpro2"),
    
    path('uviewresult/', views.uviewresult, name="uviewresult"),
    path('viewdetail/', views.viewdetail, name="viewdetail"),
    path('aviewresult/', views.aviewresult, name="aviewresult"),
    path('aviewdetail/', views.aviewdetail, name="aviewdetail"),
    




    



]
