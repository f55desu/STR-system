from django.shortcuts import redirect, render
# from django.http import HttpResponse
from STR.forms import TestTaskForm
from .models import TestTask

# Create your views here.
def home(request):
    tasks = TestTask.objects.order_by('-id')
    return render(request, 'STR/home.html', {'title': 'Главная страница сайта', 'tasks': tasks})
    # return HttpResponse("<h4>Hello</h4>")

def about(request):
    return render(request, 'STR/about.html')
    # return render("<h4>About</h4>")

def registration(request):
    error = ''
    if request.method == 'POST':
        form = TestTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = TestTaskForm()
    context = {
        'form': form,
        'error': error
    }

    return render(request, 'STR/registration.html', context)
