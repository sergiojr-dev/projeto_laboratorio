from django.urls import path
from .views.index import Index
from .views.login import Login
from .views.logout import Logout
from .views.signup import Signup
from .views.update_register import UpdateUser


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('signup/', Signup.as_view(), name='signup'),
    path('atualizar_usuario/<int:pk>', UpdateUser.as_view(), name='atualizar_usuario'),
]
