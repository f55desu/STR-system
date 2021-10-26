from django.shortcuts import redirect, render
from STR.forms import RegistrationForm, LoginForm
# from django.http import HttpResponse
import sqlite3
from django.contrib import auth
from .models import Teacher

con = sqlite3.connect("db.sqlite3")  # подключение к базе данных
curs = con.cursor()

# Create your views here.
def home(request):
    # if request.user.is_authenticated():
    teachers = Teacher.objects.order_by('-id')
    return render(request, 'STR/home.html', {'title': 'Главная страница сайта', 'teachers': teachers})
    # else:
    #     pass
    # return HttpResponse("<h4>Hello</h4>")

def rating(request):
    # if request.user.is_authenticated():
    return render(request, 'STR/rating.html')
    # else:
    #     pass
    # return render("<h4>About</h4>")

def registration(request):
    print(f'POST = {request}')
    error = ''
    if request.method == 'POST' and 'login_button' in request.POST:
        pass
        #form_login = LoginForm(request.POST)
        # if form_login.is_valid():
        #     login = request.POST['login']
        #     password = request.POST['password']
            
        #     curs.execute(f"SELECT * FROM STR_student WHERE login='{login}' AND password='{password}'")
        #     list=curs.fetchall()

        #     if list[0][0] == login and list[0][1]:           
        #          return redirect('home')
        #     else:
        #          error = 'Ошибка!'
    if request.method == 'POST' and 'reg_button' in request.POST:    
        form_reg = RegistrationForm(request.POST)
        if form_reg.is_valid():

            new_user = form_reg.save(commit=False)
            new_user.set_password(form_reg.cleaned_data['password'])
            new_user.save()

            return redirect('home')
        else:
            error = 'Форма была неверной'

    form_reg = RegistrationForm()
    form_login = LoginForm()
    context = {
        'form_login': form_login,
        'form_reg': form_reg,
        'error': error
    }

    return render(request, 'STR/registration.html', context)
