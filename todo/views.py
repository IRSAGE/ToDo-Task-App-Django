from django.shortcuts import render

def home(request):
    return render(request, 'main/index.html')

def add_todo(request):
    print(request)
