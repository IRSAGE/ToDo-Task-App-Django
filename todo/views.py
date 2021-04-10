from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from . models import Todo
from django.http import HttpResponseRedirect

def home(request):
    tasks = Todo.objects.all().order_by("-added_date")
    return render(request, 'main/index.html',{"taskItems" : tasks})

@csrf_exempt
def add_todo(request):
    date = timezone.now()
    content = request.POST['content']
    Todo.objects.create(added_date=date, text=content)
    
    return HttpResponseRedirect('/')


@csrf_exempt
def delete_todo(request, todoId):
    Todo.objects.get(id=todoId).delete()
    return HttpResponseRedirect('/')
