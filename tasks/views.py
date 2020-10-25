from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tasks
from .forms import TasksForm

# Create your views here.
def index(request):
    tasks = Tasks.objects.all()
    form = TasksForm()

    if request.method == "POST":
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    
    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/tasks.html', context)