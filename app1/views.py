from django.shortcuts import render

# Create your views here.
def function(request):
    return render(request,'firts.html')
def function2(request):
    return render(request,'second.html')