from django.views.generic import View
from ..models import Usuario
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin


class Dashboard(LoginRequiredMixin, View):

    def get(self, request, username):
        print({'username': 'userna'})
        user = get_object_or_404(Usuario, username=username)

        return render(request, 'dashboard.html', {'user': user})