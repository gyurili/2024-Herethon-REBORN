from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountApp.views import AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView, \
    AccountLoginView

app_name = "accountApp"
urlpatterns = [
    path('create/', AccountCreateView.as_view(), name = 'create'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name = 'detail'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),

    path('login/', AccountLoginView.as_view(template_name='accountApp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('check-email/', AccountCreateView.check_email, name='check_email'),
]