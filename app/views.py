from django.shortcuts import render

# Create your views here.
def helloworld(request):
    return render(request,'helloworld.html')
def python(request):
    return render(request,'python.html')
def aws(request):
    return render(request,'aws.html')
def web(request):
    return render(request,'web.html')