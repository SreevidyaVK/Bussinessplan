from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'user/index.html')

def purpose(request):
    return render(request,'user/purpose.html')

def activity(request):
    return render(request,'user/activity.html')
