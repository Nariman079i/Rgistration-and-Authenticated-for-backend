from django.contrib.auth import *
from django.contrib.auth.views import *
from django.http import request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import *
from django.views.generic import *
from .forms import RegistrationForm, AddDataUser
from .models import *


class RegisterUser(CreateView):
    form_class = RegistrationForm
    template_name = 'main/registration.html'
    success_url = reverse_lazy('login')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'main/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(requests):
    logout(requests)
    return redirect('home')


def index(requests):
    context = dict()
    file = 'main/index.html'
    if not requests.user.is_authenticated:
        return redirect('login')
    else:
        try:
            data = DataUser.objects.get(id_user=requests.user.pk)
            context['data'] = data
            context['form'] = None

        except:
            context['username'] = requests.user.username
            if requests.method == 'POST':

                form = AddDataUser(requests.POST, requests.FILES)
                if form.is_valid():
                    data_d = form.cleaned_data
                    data_user = dict(
                        id_user=requests.user.id,
                        Logo=data_d['Logo'],
                        Age=data_d['Age'],
                        Status=data_d['Status']
                    )

                    DataUser.objects.create(data_user)
                    DataUser.save()

                    return redirect('profile')
            else:
                context['form'] = AddDataUser()



    return render(requests, file, context=context)


def profile_user(requests):
    file = 'main/profile.html'
    if not requests.user.is_authenticated:
        return redirect('login')
    else:
        data = DataUser.objects.get(id_user=requests.user.id)
        data_user = dict(
            name=data.id_user.username,
            logo=data.Logo,
            age=data.Age,
            status=data.Status
        )
        context = dict(userdata=data_user)
    return render(requests, file, context=context)
