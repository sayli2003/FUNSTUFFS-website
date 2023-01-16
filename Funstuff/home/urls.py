from django.contrib import admin
from django.urls import path
from home import views
from home import databse as db
import sqlite3



def titles():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    data = db.tolist(cursor,0)
    for title in data:
        urlpatterns.append(path(title["name"],v(title["name"]),name=title["name"]))
        print("here")
        print(title)
    
    
def v(x):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    data = db.find(x, cursor)
    if data is False:
        views.data={}
    else:
        views.data=data
    return views.view

urlpatterns=[
    path("",views.index,name="home"),
    path("view",views.view,name="view"),
    path("work",titles),
]
titles()