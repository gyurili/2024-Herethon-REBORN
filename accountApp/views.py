from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
# from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from mainApp.models import Post
from .decorators import account_ownership_required
from .models import User
from .forms import AccountCreationForm, AccountLoginForm

has_ownership = [
    account_ownership_required, login_required
]

# Create your views here.
class AccountCreateView(CreateView):
    model = User
    form_class = AccountCreationForm
    success_url = reverse_lazy('accountApp:login')
    context_object_name = 'target_user'
    template_name = 'accountApp/create.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        print("Form is valid")
        messages.success(self.request, '회원가입이 완료되었습니다. 로그인 해주세요.')
        return response

    def form_invalid(self, form):
        print("Form is invalid")
        print(form.errors)
        return super().form_invalid(form)

    @staticmethod
    def check_email(request):
        email = request.GET.get('email', None)
        is_taken = User.objects.filter(email=email).exists()
        data = {
            'is_taken': is_taken
        }
        return JsonResponse(data)

    @staticmethod
    def check_nickname(request):
        nickname = request.GET.get('nickname', None)
        is_taken = User.objects.filter(nickname=nickname).exists()
        data = {
            'is_taken': is_taken
        }
        return JsonResponse(data)


class AccountLoginView(LoginView):
    authentication_form=AccountLoginForm
    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password.')
        return super().form_invalid(form)

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountApp/detail.html'

    def get_context_data(self, **kwargs):
        user = self.get_object()
        post_list = Post.objects.filter(author=user)
        liked_post_list = Post.objects.filter(post_likes__user=user)

        context = super(AccountDetailView, self).get_context_data(post_list=post_list, **kwargs)
        context['liked_post_list'] = liked_post_list

        return context



@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountApp/update.html'
    success_url = reverse_lazy('mainApp:main')
    form_class = AccountCreationForm


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView) :
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('mainApp:main')
    template_name = 'accountApp/delete.html'

