from django.views import View
from django.shortcuts import render, redirect
from ..forms.login_forms import LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login


class Login(View):
    def get(self, request):
        form = LoginForm
        formulario = {'form': form}

        return render(request, 'login.html', formulario)
    
    def post(self, request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                return redirect('dashboard')
            
            else:
                messages.error(request, 'Credenciais invalidas.')

                return render(request, 'login.html')