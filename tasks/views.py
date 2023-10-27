from django.shortcuts import render, redirect
from django.http import HttpResponse

from . models import *
from . forms import *


# Create your views here.
def index(request):
    tasks =task.objects.all()
    form=TaskForm()

    if request.method =='POST':
        form= TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context= {'tasks':tasks, 'form':form}
    return render(request, 'tasks/lists.html', context)


def updatetask(request,pk):

    Task = task.objects.get(id=pk)
    form = TaskForm(instance=Task)

    if request.method=='POST':
        form=TaskForm(request.POST, instance=Task)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context ={'form':form}
    return render(request,'tasks/update_task.html', context)

def delete(request, pk):
    item=task.objects.get(id=pk)
    
    if request.method=='POST':
        item.delete()
        return redirect('/')

    context ={'item':item}
    return render(request,'tasks/delete_task.html', context)
