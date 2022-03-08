from django.shortcuts import render

# Create your views here.

# creating home screen 
def Home(request):
    return render(request, 'index.html')
