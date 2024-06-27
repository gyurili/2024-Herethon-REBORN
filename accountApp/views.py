from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

from .decorators import account_ownership_required
from .models import User
from .forms import AccountCreationForm

has_ownership = [
    account_ownership_required, login_required
]

# Create your views here.


class TestHomeView(ListView):
    model = User
    template_name = 'accountApp/testhome.html'


class AccountCreateView(CreateView):
    model = User
    form_class = AccountCreationForm
    success_url = reverse_lazy('accountApp:detail')
    context_object_name = 'target_user'
    template_name = 'accountApp/create.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        print("Form is valid")
        return response

    def form_invalid(self, form):
        print("Form is invalid")
        print(form.errors)
        return super().form_invalid(form)

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountApp/detail.html'

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountApp/update.html'
    success_url = reverse_lazy('accountApp:testhome')
    form_class = AccountCreationForm

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView) :
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountApp:testhome')
    template_name = 'accountApp/delete.html'


