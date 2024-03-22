from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
from myapp.models import ToDo

# Create your views here.

def home(request):
    todo_items = ToDo.objects.all().order_by('-added_date')

    return render(request, 'myapp/index.html', { 'todo_items': todo_items })

def add_todo(request):
    current_date = timezone.now()
    content = request.POST["content"]
    created_objects = ToDo.objects.create(added_date=current_date, text=content)

    return HttpResponseRedirect("/")

def delete_todo(request, todo_id):
    ToDo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")