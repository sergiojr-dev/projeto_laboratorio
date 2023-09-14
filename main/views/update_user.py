from django.views.generic.edit import UpdateView
from ..models import Usuario
from ..forms.updateuser_forms import UserUpdateForm
from django.urls import reverse_lazy


class UpdateUser(UpdateView):
    model = Usuario
    form_class = UserUpdateForm
    template_name = 'update_user.html'
    success_url = reverse_lazy('dashboard') 