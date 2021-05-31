from django.shortcuts import render, redirect
from todos.forms import TodoForm
from .models import Todos

from .models import Todos


# Create your views here.
def todo_create(request):
    form = TodoForm()
    context = {}
    context["form"] = form
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            # print("save")

    return render(request, "todos/todocreate.html", context)


def todo_list(request):
    # form=TodoForm()
    todos = Todos.objects.all()
    context = {}
    context['todos'] = todos
    return render(request, "todos/todolist.html", context)


def todo_detail(request,id):
    todo = Todos.objects.get(id=id)
    context = {}
    context['todo'] = todo
    return render(request, "todos/tododetail.html", context)

def todo_update(request,id):
    todo=Todos.objects.get(id=id)
    form=TodoForm(instance=todo)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=TodoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect("list")
    return render(request,"todos/todoupdate.html",context)
def todo_delete(request,id):
    todo=Todos.objects.get(id=id)
    todo.delete()
    return redirect("list")
