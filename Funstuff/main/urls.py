from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="Initail"),
    path("art/<str:t>", views.seeArt, name='Art'),
]
