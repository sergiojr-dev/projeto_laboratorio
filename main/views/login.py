from django.views import View
from django.shortcuts import render
from ..forms.login_forms import LoginForm


class Login(View):
    def get(self, request):
        form = LoginForm
        formulario = {'form': form}
        return render(request, 'login.html', formulario)