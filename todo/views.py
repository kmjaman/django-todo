from django.shortcuts import get_object_or_404, redirect, render
from todo.forms import TodoForm

from todo.models import TodoList

# Create your views here.

def index(request):

	item_list = TodoList.objects.order_by("-id")
	if request.method == "POST":
		form = TodoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('index')
	form = TodoForm()

	context = {
			"forms" : form,
			"list" : item_list,
		}
	return render(request, 'index.html', context)

def delete(request, id):    
    todo = get_object_or_404(TodoList, id=id)
    todo.delete()
    return redirect('index')