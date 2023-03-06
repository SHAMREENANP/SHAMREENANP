from django.shortcuts import render

# Create your views here.
def loadfisrtpage(request):
    return render(request,'first.html')
def loadsecondpage(request):
    return render(request,'second.html')
def loadtwono(request):
    return render(request,'add.html')
def loadnumbers(request):
    n1=int(request.GET.get('number1'))
    n2=int(request.GET.get('number2'))
    sum=n1+n2
    return render (request,'resultnum.html',{'result':sum})