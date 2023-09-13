from django.views.generic import View
from ..models import Usuario
from django.shortcuts import render, get_object_or_404

class Dashboard(View):

        # def get(self, request):

        #     return render(request, 'dashboard.html')


    def get(self, request, username):
        print({'username': 'userna'})
        user = get_object_or_404(Usuario, username=username)

        return render(request, 'dashboard.html', {'user': user})