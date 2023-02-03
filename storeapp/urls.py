from django.urls import path,include
from  storeapp import views 

urlpatterns= [
    path('', views.homeview, name="home"),
    path('about/',views.aboutview, name="about"),
    path('course/',views.course, name="course"),
    path('contact/',views.cotact, name="contact"),
    path('login/',views.loginpage, name="login"),
    path('register/',views.registerpage, name="register"),
]