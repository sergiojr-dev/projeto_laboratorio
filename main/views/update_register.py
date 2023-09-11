from django.views.generic.edit import UpdateView
from ..models import Usuario
from ..forms.update_registration_forms import UpdateRegisterForm
from django.urls import reverse_lazy


class UpdateUser(UpdateView):
    model = Usuario
    form_class = UpdateRegisterForm
    template_name = 'update_user.html'
    success_url = reverse_lazy('signup') # alterar para a pagina correta depois