from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Task

def index(request):
  if request.method == 'POST':
    task = Task(description = request.POST['description'])
    task.save()
  tasks = Task.objects.all()
  context = {'tasks': tasks}
  return render(request, 'tasks/index.html', context)
