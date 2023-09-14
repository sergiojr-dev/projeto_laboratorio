from django import forms
from ..models import Usuario

class UserUpdateForm(forms.ModelForm):
    USUARIO = [
        (1, 'Aluno'),
        (2, 'Professor')
    ]
    class Meta:
        model= Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'is_active', 'user', 'cpf_cnpj', 'phone']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Nome de usuário'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Primeiro nome'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Sobrenome'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Endereço de email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Senha'}),
            'is_active': forms.CheckboxInput(attrs={'placeholder': 'Ativo'}),
            'cpf_cnpj': forms.TextInput(attrs={'placeholder': 'CPF/CNPJ'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Telefone'}),
        }

    #user = forms.ChoiceField(choices=USUARIO, widget=forms.Select(attrs={'placeholder': 'Usuário'}))
    user = forms.ChoiceField(
        choices=[('', 'Selecione...')] + USUARIO,  # Adiciona "Selecione..." como a primeira opção
        widget=forms.Select(attrs={'placeholder': 'Usuário'})
    )