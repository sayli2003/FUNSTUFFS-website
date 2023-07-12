from django.urls import path
from . import views

urlpatterns = [
    path('',views.dash,name="Initail"),
    path('dash/',views.dash,name='DashBoard'),
    path('login/',views.log,name="Signin"),
    path('add/',views.addartwork,name="Signin"),

]
