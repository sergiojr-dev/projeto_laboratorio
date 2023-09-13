from django.views import View
from django.shortcuts import render, redirect
from ..forms.login_forms import LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login


class Login(View):
    def get(self, request):
        form = LoginForm()
        formulario = {'form': form}

        return render(request, 'login.html', formulario)
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                return redirect('dashboard', username=request.user.username)
            
        messages.error(request, 'Credenciais invalidas.')
        form = LoginForm()
        formulario = {'form': form}
        return render(request, 'login.html', formulario)