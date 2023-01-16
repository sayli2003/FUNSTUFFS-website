from django.shortcuts import render
from home.databse import *
import sqlite3

from django.urls import path,include

data={}
def index(request):
    dir = "C://Users//Sayli//PycharmProjects//webdev//Funstuff//static//images"
    conn = sqlite3.connect('data.db')
    cursor=conn.cursor()
    # cursor.execute("DROP TABLE artwork")
    # cursor.execute("CREATE TABLE artwork(title,description,link,comments)")
    # conn.commit()
    # read(dir,conn)
    li=tolist(cursor,3)
    context = {
        'image_url_1': '/static/images/Lovely Fluid In%20Soft%20Pink%20Background.jpeg',
        'myface':'/static/images/my.jpeg',
        'view_page_url': 'view'
    }
    context['li']=li
    return render(request,'new_index.html',context)

def view(request):
    conn = sqlite3.connect('data.db')
    cursor=conn.cursor()
    context={}
    context["data"]=data
    context["comments"]=getcomments(cursor,data['comments'])
    return render(request,'view_the_art.html',context)
