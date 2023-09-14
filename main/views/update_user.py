from django.views.generic.edit import UpdateView
from ..models import Usuario
from ..forms.updateuser_forms import UserUpdateForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class UpdateUser(LoginRequiredMixin, UpdateView):
    model = Usuario
    form_class = UserUpdateForm
    template_name = 'update_user.html'
    success_url = reverse_lazy('dashboard') 