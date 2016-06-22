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

#def login(request):
    #if request.method == 'POST'


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
