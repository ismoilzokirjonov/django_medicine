from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"dashboard.html")  

def medicine(request):
    return render(request,"medicine.html")
    