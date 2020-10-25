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


def update_task(request, pk):

    task = Tasks.objects.get(id=pk)

    form = TasksForm(instance=task)

    if request.method == "POST":
        form = TasksForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect(index)

    context = {'form': form}
    return render(request, 'tasks/update.html', context)


def delete_task(request, pk):

    task = Tasks.objects.get(id=pk)
    context = {'task':  task}

    if request.method ==  "POST":
        task.delete()
        return redirect('/')

    return render(request, 'tasks/delete.html', context)