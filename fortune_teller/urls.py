from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import register  # Import your register view
from django.urls import path, include # new
from .forms import UserSetPasswordForm
from django.urls import reverse_lazy



urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='fortune_teller/account/login.html'), name='login'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/register/done', views.register_done, name="account_activation_sent"),
    path('account/register/<uidb64>/<token>/', views.activate, name='register_activate'),
    path('account/register/done/', views.register_complete, name='register_complete'),
    path('accounts/info/', views.user_info, name='account_info'),

    path('accounts/profile/', views.user_fortunes, name='user_fortunes'),

    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(template_name='fortune_teller/account/password_reset.html'), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='fortune_teller/account/password_reset_done.html'), name='password_reset_done'),
    path('accounts/password_reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='fortune_teller/account/password_reset_confirm.html', success_url=reverse_lazy('password_reset_complete')), name='password_reset_confirm'),
    #path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name ='password_reset_confirm'),

    path('accounts/password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='fortune_teller/account/password_reset_complete.html'), name='password_reset_complete'),


    #path("accounts/", include("django.contrib.auth.urls")),
    path('add_fortune/', views.add_fortune, name='add_fortune'),
    path('fortunes/', views.view_fortunes, name='view_fortunes'),
    path('fortunes/edit/<int:fortune_id>/', views.edit_fortune, name='edit_fortune'),

    path('history/', views.history, name='history'),
    path('info/', views.user_info, name='user_info'),
    path("clear_cookies/", views.clear_cookies, name="clear_cookies"),
    path('fortunes/<int:fortune_id>/', views.view_fortune, name='view_fortune'),
]
