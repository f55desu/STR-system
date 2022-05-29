from time import time
from tokenize import group
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

from .tokens import account_activation_token
from django.core.mail import EmailMessage

from django.shortcuts import redirect, render
from django.contrib.auth import login, logout

from .forms import AttendanceForm, GetTeacherForm, GetGroupForm, LoginForm, RegistrationForm
from .models import *

from . import AvgRatingFunc

def str(request):
    if not request.user.is_authenticated:
        return redirect('registration')
    if not request.user.is_student:
        return redirect('registration')

    if request.method == 'POST' and 'button_logout' in request.POST:
        logout(request)
        return redirect('registration')
    if request.method == 'POST' and 'save_button' in request.POST:
        teacher_subject = request.POST.get('id_input')

        print(f'\nID_TEACHER = {teacher_subject}')
        print(request.POST)

        for crit in Criterion.objects.order_by('id'):
            gradeObj = Grade.objects.filter(student=request.user.student, criterion=crit, teacher_subject=teacher_subject)
            print(f'GRADE_OBJ = {gradeObj}')

            if gradeObj:
                print(f'CRIT_ID = {crit.id}')
                my_grade = request.POST.get(f'rating{crit.id}')

                if my_grade:
                    print(f'MY_GRADE = {my_grade}')
                    gradeObj.update(grade=my_grade)


    subjects_groups = Subject_Group.objects.filter(group=request.user.student.group).all()
    teachers_subjects = Teacher_Subject.objects.order_by('id')
    criterions = Criterion.objects.order_by('id')
    grades = Grade.objects.filter(student=request.user.student)

    curr_teacher_subjects = []
    for subject_group in subjects_groups:
        for teacher_subject in teachers_subjects:
            if teacher_subject.subject == subject_group.subject:
                curr_teacher_subjects.append(teacher_subject)

    if not grades or len(curr_teacher_subjects) != len(grades) / len(criterions):
        for subject_group in subjects_groups:
            for teacher_subject in teachers_subjects:
                if teacher_subject.subject == subject_group.subject:
                    for crit in criterions:
                        if not Grade.objects.filter(teacher_subject=teacher_subject, student=request.user.student, criterion=crit).exists():
                            newGrade = Grade(teacher_subject=teacher_subject, student=request.user.student, criterion=crit)
                            newGrade.save()
        
    # for grade in grades:
    #     print(f"\nGRADE: {grade}")

    data = AvgRatingFunc.avg(curr_teacher_subjects, Grade.objects.all(), criterions, request.user)
    print(f"\n\n\n {data}")

    context = {
        'title': 'Главная страница сайта',
        'criterions': criterions,
        'data': data,
    }
    
    return render(request, 'STR/str.html', context)

def home(request):
    #print(Group.objects.values_list('name'))
    # groups = Group.objects.values_list('name', flat=True)
    schedules = None
    # Отчаяние
    # schedulesMonday800 = None
    # schedulesMonday945 = None
    # schedulesMonday1130 = None
    # schedulesTuesday = None
    # schedulesWednesday = None
    # schedulesThursday = None
    # schedulesFriday = None
    # schedulesSaturday = None
    currGroup = None
    currTeacher = None

    groupForm = GetGroupForm()
    teacherForm = GetTeacherForm()

    attendanceForm = AttendanceForm(request=request)

    if request.method == 'POST' and 'button_logout' in request.POST:
        logout(request)
        return redirect('registration')
    if request.method == 'POST' and 'to_str' in request.POST:
        return redirect('str')
    if request.method == 'POST' and 'select_group' in request.POST:
        # groupNameToFind = ''
        # for i in range(0, len(groups)):
        #     if int(request.POST['group_name']) == i:
        #         groupNameToFind = groups[i]
        #         break
        # Если выбрана группа
        if request.POST['group_name'] != '':
            currGroup = request.POST['group_name']
            group = Group.objects.filter(name=request.POST['group_name'])

            schedules = Schedule.objects.filter(group__in=group)
            # Отчаяние
            # schedulesMonday800 = Schedule.objects.filter(group__in=Group.objects.filter(name=request.POST['group_name']), weekday='Понедельник', time='C 8:00 до 9:30')
            # schedulesMonday945 = Schedule.objects.filter(group__in=Group.objects.filter(name=request.POST['group_name']), weekday='Понедельник', time='С 9:45 до 11:15')
            # schedulesMonday1130 = Schedule.objects.filter(group__in=Group.objects.filter(name=request.POST['group_name']), weekday='Понедельник', time='С 11:30 до 13:15')
            # schedulesTuesday = Schedule.objects.filter(group__in=Group.objects.filter(name=request.POST['group_name']), weekday='Вторник')
            # schedulesWednesday= Schedule.objects.filter(group__in=Group.objects.filter(name=request.POST['group_name']), weekday='Среда')
            # schedulesThursday = Schedule.objects.filter(group__in=Group.objects.filter(name=request.POST['group_name']), weekday='Четверг')
            # schedulesFriday = Schedule.objects.filter(group__in=Group.objects.filter(name=request.POST['group_name']), weekday='Пятница')
            # schedulesSaturday = Schedule.objects.filter(group__in=Group.objects.filter(name=request.POST['group_name']), weekday='Суббота')
        # Если выбран препод
        if request.POST['teacherName'] != '':
            currTeacher = f"{request.POST['teacherName'][:-1]}ва"
            teacher = Teacher.objects.filter(user__surname=request.POST['teacherName'])

            schedules = Schedule.objects.filter(teacher__in=teacher)

        # Если выбран препод и группа
        if request.POST['teacherName'] != '' and request.POST['group_name'] != '':
            currGroup = request.POST['group_name']

            currTeacher = f"{request.POST['teacherName'][:-1]}ва"
            teacher = Teacher.objects.filter(user__surname=request.POST['teacherName'])

            group = Group.objects.filter(name=request.POST['group_name'])

            schedules = Schedule.objects.filter(teacher__in=teacher, group__in=group)

        # if schedules:
        #     currGroup = request.POST['group_name']
        #     currTeacher = f"{request.POST['teacherName'][:-1]}ва"
        #     print(currGroup)
        #     print(currTeacher)
        # else:
        #     currGroup = request.POST['group_name']
        #     currTeacher = request.POST['teacherName']

        if schedules:
            schedules = schedules.order_by('weekday', 'time_range', '-even_week', 'subgroup_number')

            schedules_subgroup_1 = schedules.filter(subgroup_number__in=[0, 1])
            schedules_subgroup_2 = schedules.filter(subgroup_number__in=[0, 2])

            schedules = list(zip(schedules_subgroup_1, schedules_subgroup_2))

            # schedules = list(zip(schedules_subgroup_1, schedules_subgroup_2))          

            # for item in list(schedules):
            #     print(f'\n{item}')

    context = {
        'groupForm': groupForm,
        'teacherForm': teacherForm,
        'schedules': schedules,
        # Отчаяние
        # 'schedulesMonday800': schedulesMonday800,
        # 'schedulesMonday945': schedulesMonday945,
        # 'schedulesMonday1130': schedulesMonday1130,
        # 'schedulesTuesday': schedulesTuesday,
        # 'schedulesWednesday': schedulesWednesday,
        # 'schedulesThursday': schedulesThursday,
        # 'schedulesFriday': schedulesFriday,
        # 'schedulesSaturday': schedulesSaturday,
        'currGroupName': currGroup,
        'currTeacher': currTeacher,
        'attendanceForm': attendanceForm,
    }
    currGroup = None
    currTeacher = None
    return render(request, 'STR/home.html', context)

def registration(request):
    if request.user.is_authenticated:
        return redirect('home')

    # error = ''
    if request.method == 'POST' and 'login_button' in request.POST:
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = login_form.login(request)
            if user:
                login(request, user)
                return redirect('home')

        form = RegistrationForm()
        context = {
            # 'form_login': form_login,
            'login_form': login_form,
            'form': form,
        }

        return render(request, 'STR/registration.html', context)

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
            mail_subject = 'СОП. Активация аккаунта.'
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()

            return redirect('acc_active_sent')
        
        login_form = LoginForm
        context = {
            # 'form_login': form_login,
            'login_form': login_form,
            'form': form,
        }

        return render(request, 'STR/registration.html', context)

    elif request.method == 'POST' and 'button_logout' in request.POST:
        logout(request)
        return redirect('registration')

    login_form = LoginForm()
    form = RegistrationForm()
    # form_login = None
    context = {
        # 'form_login': form_login,
        'login_form': login_form,
        'form': form,
    }

    return render(request, 'STR/registration.html', context)

# активация акков
def acc_active_sent(request):
    return render(request, 'STR/acc_active_sent.html')

def acc_active_confirmed(request):
    if request.method == 'POST' and 'back_button' in request.POST:
        return redirect('registration')
    return render(request, 'STR/acc_active_confirmed.html')

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
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



