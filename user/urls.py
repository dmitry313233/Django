from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from user.apps import UserConfig
from user.views import RegisterView, UserUpdateView, generate_new_password, Verifi

app_name = UserConfig.name


urlpatterns = [
    path('', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('registration/', RegisterView.as_view(), name='registration'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('verification/', Verifi, name='verification'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('profile/genpassword/', generate_new_password, name='generate_new_password'),

]
