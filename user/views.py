import random
import secrets

from django.conf import settings
from django.contrib.auth.views import LoginView as BaseLoginView
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, TemplateView

from user.forms import UserRegisterForm, UserForm
from user.models import User


# class LoginView(BaseLoginView):
#     model = User
#     form_class = LoginForm
#     template_name = 'user/login.html'

# class Logout()

# Create your views here.

class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'user/registration.html'
    success_url = reverse_lazy('user:verifymessage')

    def form_valid(self, form):
        if form.is_valid():
            instance = form.save(commit=False)
            cod = ''.join([str(random.randint(1, 10)) for i in range(5)])  # это ссылка высылается по почте
            instance.cod = cod
            url = reverse('user:verification', args=[cod])
            total_url = self.request.build_absolute_uri(url)
            send_mail(
                subject='Успешная верификация',
                message=f'Пройдите по ссылке для успешной верификации: {total_url}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[instance.email]
            )
            instance.save()
            return super().form_valid(form)


def verify(request, cod):  # Это контролер на FBV
    user = User.objects.get(cod=cod)
    user.is_active = True
    user.save()
    return redirect(reverse('user:login'))


class Verifymessage(TemplateView):
    model = User
    template_name = 'user/verifymessage.html'



    # def form_valid(self, form):
    #     if form.is_valid():
    #         instance = form.save(commit=False)
    #         verification = ''.join([str(random.randint(1, 10)) for i in range(12)])  # это ссылка высылается по почте
    #         instance.cod = verification
    #         send_mail(
    #             subject='Вы сменили пароль',
    #             message=f'Ваш новый пароль: {verification}',
    #             from_email=settings.EMAIL_HOST_USER,
    #             recipient_list=[instance.email]
    #         )
    #         instance.save()
    #         return super().form_valid(form)


# class VerificationView(CreateView):
#     model = User
#     form_class = UserVerificationForm
#     template_name = 'user/verification.html'

# def Verifi(request):
#     if request.method == 'POST':
#         cod = request.POST.get('cod')
#         email = request.POST.get('email')
#         user = User.objects.get(email=email)
#         if user.cod == cod:
#             user.is_active = True
#             user.save()
#             return redirect(reverse('user:login'))
#     return render(request, 'user/verification.html')


class UserUpdateView(UpdateView):  # Сможем редактировать текущего пользователя
    model = User
    success_url = reverse_lazy('user:profile')
    form_class = UserForm
    template_name = 'user/profile.html'

    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    new_password = ''.join([str(random.randint(0, 9)) for _ in range(13)])
    print(new_password)
    send_mail(
        subject='Вы сменили пароль',
        message=f'Ваш новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('user:login'))
