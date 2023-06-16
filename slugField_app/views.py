from django.shortcuts import render
from .models import *
# Create your views here.


def show(request):

    a = Student.objects.all()
    return render(request,'show.html',{'a':a})

def readmore(request,slug):
    data = Student.objects.get(slug=slug)

    return render(request,'readmore.html',{'data':data})