from django.shortcuts import render

# Create your views here.
def csk(request):
    return render(request,'csk.html')


def mi(request):
    return render(request,'mi.html')
