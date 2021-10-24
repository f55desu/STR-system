from django.shortcuts import redirect, render
from STR.forms import RegistrationForm
# from django.http import HttpResponse
from .models import Student

# Create your views here.
def home(request):
    students = Student.objects.order_by('-id')
    return render(request, 'STR/home.html', {'title': 'Главная страница сайта', 'tickets': students})
    # return HttpResponse("<h4>Hello</h4>")

def rating(request):
    return render(request, 'STR/rating.html')
    # return render("<h4>About</h4>")

def registration(request):
    error = ''
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = RegistrationForm()
    context = {
        'form': form,
        'error': error
    }

    return render(request, 'STR/registration.html', context)
