from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm

def todo_list(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        selected_todos = request.POST.getlist('selected_todos')
        
        if action == 'delete':
            Todo.objects.filter(id__in=selected_todos).delete()
        
        return redirect('todo_list')

    todos = Todo.objects.all()
    return render(request, 'todo/todo_list.html', {'todos': todos})

def complete_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.completed = True
    todo.save()
    return redirect('todo_list')

def add_todo(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        completed = request.POST.get('completed') == 'on'
        Todo.objects.create(text=text, completed=completed)
        return redirect('todo_list')

    return render(request, 'todo/add_todo.html')

def edit_todo(request, id):
    todo = get_object_or_404(Todo, id=id)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)

    return render(request, 'todo/edit_todo.html', {'form': form, 'todo': todo})
