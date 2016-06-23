from django.shortcuts import render
from user_related.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    return render(request, 'user_related/index.html', {})


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
    else:
        user_form = UserForm()

    return render(request, 'user_related/register.html', {
        'user_form': user_form,
        'registered': registered
    }
            )


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user:
            if user.is_active():
                login(request, user)
                return HttpResponseRedirect('/index/')
            else:
                return HttpResponse('您的账户目前不可用')
        else:
            print("您输入的邮箱地址或密码有误: \n{0},\n{1}".format(email, password))
            return HttpResponse("请重新输入")
    else:
        return render(request, 'user_related/login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/index/')


@login_required
def add_information(request):
    if request.method == 'POST':
        userprofile_form = UserProfileForm(request.POST)

    context = {}
    render(request, 'user_related/add_information.html', context)
