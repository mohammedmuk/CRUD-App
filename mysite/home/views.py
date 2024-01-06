from django.shortcuts import render
from django.views import View
from django.conf import settings
from django.contrib.auth.models import User, auth
from django.shortcuts import redirect, render

# Create your views here.

# This is a little complex because we need to detect when we are
# running in various configurations


class HomeView(View):
    def get(self, request):
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal
        }
        return render(request, 'home/main.html', context)


def sign_up(request):
    if request.method == 'POST':
        user = request.POST['username']
        mail = request.POST['email']
        pas = request.POST['password']
        pas2 = request.POST['password2']

        if user and mail and pas:
            if pas == pas2:
               if User.objects.filter(email=mail).exists():
                  ctx = {'error_email' : 'This email used by another user'}
                  return render(request, 'registration/signup.htm', ctx)

               elif User.objects.filter(username=user).exists():
                  ctx = {'error_username' : 'This username used by another user'}
                  return render(request, 'registration/signup.htm', ctx)

               else:
                  usr = User.objects.create_user(username=user, email=mail, password=pas)
                  usr.save()
                  user_login = auth.authenticate(username=user, password=pas)
                  auth.login(request, user_login)
                  return redirect(request.GET['next'])

            else:
              ctx = {'error_password' : 'Passwords doesn,t match'}
              return render(request, 'registration/signup.htm', ctx)
        else:
           ctx = {"error_form" : 'All fields are required'}
           return render(request, 'registration/signup.htm', ctx)
    
    elif request.method == 'GET':
        return render(request, 'registration/signup.htm', {})