from django.shortcuts import render

# Create your views here.
def rcb(request):
    return render(request,'rcb.html')


def srh(request):
    return render(request,'srh.html')
