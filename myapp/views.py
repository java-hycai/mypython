from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello(request):
    return render(request, "template/hello.html", {})

def hello2(request,id):
    return render(request, "template/hello2.html", {"id",id})