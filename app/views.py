from django.shortcuts import render

# Create your views here.
def forloop(request):
    d={'Name':'venky'}
    return render(request,'forloop.html',context=d)