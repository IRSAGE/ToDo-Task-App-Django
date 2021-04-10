from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from . models import Todo

def home(request):
    return render(request, 'main/index.html')

@csrf_exempt
def add_todo(request):
    date = timezone.now()
    content = request.POST['content']
    Todo.objects.create(added_date=date, text=content)
    
    return render(request, 'main/index.html')
