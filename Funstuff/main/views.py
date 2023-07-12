from django.shortcuts import render
from host.models import AddArt
import numpy as np

# Create your views here.
def index(request):
    context={}
    context["items"]=list(range(5))
    li=AddArt.objects.all()
    i=0
    count=0
    newli=[]
    k=[]
    while(i<len(li)):
        if count==3:
            newli.append(k)
            k=[]
            count=0
        k.append(li[i])
        i+=1
        count+=1
    newli.append(k)
    print(newli)
        
    context["art"]=newli
    return render(request,"index.html",context)

def seeArt(request,t):
    context={}
    context["item"]=AddArt.objects.all()
    print(context["item"])
    return render(request,"viewpage.html",context)