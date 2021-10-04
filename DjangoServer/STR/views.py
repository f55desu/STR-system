from django.shortcuts import redirect, render
from STR.forms import TicketForm
# from django.http import HttpResponse
from .models import Ticket

# Create your views here.
def home(request):
    tickets = Ticket.objects.order_by('-id')
    return render(request, 'STR/home.html', {'title': 'Главная страница сайта', 'tickets': tickets})
    # return HttpResponse("<h4>Hello</h4>")

def about(request):
    return render(request, 'STR/about.html')
    # return render("<h4>About</h4>")

def registration(request):
    error = ''
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = TicketForm()
    context = {
        'form': form,
        'error': error
    }

    return render(request, 'STR/registration.html', context)
