from django.shortcuts import render, redirect
from .models import apptodo
from django.contrib.auth.decorators import login_required
from .forms import AddTodoForm

# Create your views here.
@login_required
def home(request):
    form = AddTodoForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        form = AddTodoForm()

    list_ = apptodo.objects.filter(user = request.user)
    context = {
        'list': list_,
		'form' : form,
    }
    return render(request, "apptodo/home.html", context)

@login_required
def delete_item(request, id):
    apptodo.objects.get(pk=id).delete()
    return redirect('/todo/')