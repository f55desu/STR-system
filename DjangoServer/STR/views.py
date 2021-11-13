from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.utils.encoding import force_text

from django.shortcuts import redirect, render
# from STR.forms import RegistrationForm, LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# import json

# from django.http import HttpResponse
# import sqlite3
from django.contrib import auth

from .forms import RegistrationForm
from .models import Teacher

from . import AvgRatingFunc
# from DjangoServer import STR

# con = sqlite3.connect("db.sqlite3")  # подключение к базе данных
# curs = con.cursor()

# Create your views here.
def home(request):
    if request.method == 'POST' and 'button_logout' in request.POST:
        auth.logout(request)
        return redirect('registration')
    if request.method == 'GET' and 'save_button' in request.GET:
        id_Teacher = request.GET.get('id_input')
        print(f'ID_TEACHER:{id_Teacher}')
        print(request.GET)
        rating1 = request.GET.get('rating1')
        if rating1 == None:
            rating1 = 0.0
        rating2 = request.GET.get('rating2')
        if rating2 == None:
            rating2 = 0.0
        rating3 = request.GET.get('rating3')
        if rating3 == None:
            rating3 = 0.0
        rating4 = request.GET.get('rating4')
        if rating4 == None:
            rating4 = 0.0
        overall = AvgRatingFunc.avg(list([float(rating1), float(rating2), float(rating3), float(rating4)]))
        print(f'Rating overall: {overall}')
    # if request.user.is_authenticated():
    teachers = Teacher.objects.order_by('-id')
    return render(request, 'STR/home.html', {'title': 'Главная страница сайта', 'teachers': teachers})
    # else:
    #     pass
    # return HttpResponse("<h4>Hello</h4>")

def rating(request):
    if request.method == 'GET' and 'save_button' in request.GET:
        rating1 = request.GET.get('rating1')
        if rating1 == None:
            rating1 = 0.0
        rating2 = request.GET.get('rating2')
        if rating2 == None:
            rating2 = 0.0
        overall = AvgRatingFunc.avg(list([float(rating1), float(rating2)]))
        print(f'Rating overall: {overall}')
    return render(request, 'STR/rating.html')

def acc_active_sent(request):
    return render(request, 'STR/acc_active_sent.html')

def registration(request):

    if request.user.is_authenticated:
        return redirect('home')

    error = ''
    if request.method == 'POST' and 'login_button' in request.POST:
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        user = auth.authenticate(email=email, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect('home')
        else:
            # error msg
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
    elif request.method == 'POST' and 'reg_button' in request.POST:    
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            current_site = get_current_site(request)
            message = render_to_string('STR/acc_active_email.html', {
                'user': user, 'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            # Sending activation link in terminal
            # user.email_user(subject, message)
            mail_subject = 'Activate your SOP account.'
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()

            # new_user = form_reg.save(commit=False)
            # new_user.set_password(form_reg.cleaned_data['password'])
            # new_user.save()
            # if form._meta.model.USERNAME_FIELD in form.fields:
            #     form.fields[form._meta.model.USERNAME_FIELD].widget.attrs['autofocus'] = False
            # return HttpResponse('Please confirm your email address to complete the registration.')
            return redirect('acc_active_sent')
    elif request.method == 'POST' and 'button_logout' in request.POST:
        auth.logout(request)
        return redirect('registration')
    # else:
    #     error = 'Форма была неверной'

    form = RegistrationForm()
    # form_login = None
    context = {
        # 'form_login': form_login,
        'form': form,
        'error': error
    }

    return render(request, 'STR/registration.html', context)

def acc_active_confirmed(request):
    if request.method == 'POST' and 'back_button' in request.POST:
        return redirect('registration')
    return render(request, 'STR/acc_active_confirmed.html')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = get_user_model().objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
        user = None

    print(user)
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # login(request, user)  логин в систему
        return redirect('acc_active_confirmed')
    else:
        return HttpResponse('Activation link is invalid!')
