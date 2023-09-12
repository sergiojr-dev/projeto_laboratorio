from django.views.generic import View
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

class Dashboard(View):

    # def get(self, request):

    #     return render(request, 'dashboard.html')


    def get(self, request, username):
        # username = self.kwargs['username']
        user = get_object_or_404(User, username=username)

        return render(request, 'dashboar.html', {'user': user})