from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo

def home(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        due_date = request.POST.get("due_date")

        todo = Todo(title=title, description=description)
        if due_date:
            todo.due_date = due_date
        todo.save()
        return redirect("home")

    todos = Todo.objects.all().order_by("is_completed", "due_date")
    return render(request, "home.html", {"todos": todos})


def toggle_complete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.is_completed = not todo.is_completed
    todo.save()
    return redirect("home")


def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect("home")

def edit_todo(request, pk):
    """View to edit an existing TODO item."""
    todo = get_object_or_404(Todo, pk=pk)

    if request.method == "POST":
        todo.title = request.POST.get("title")
        todo.description = request.POST.get("description")
        due_date = request.POST.get("due_date")

        if due_date:
            todo.due_date = due_date
        else:
            todo.due_date = None

        todo.save()
        return redirect("home")

    # GET request → show form pre-filled with current values
    return render(request, "edit_todo.html", {"todo": todo})
