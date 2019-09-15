from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('password-change', auth_views.PasswordChangeView.as_view(), name='password-change'),
    path('password-change-done', auth_views.PasswordChangeDoneView.as_view(), name='password-change-done'),
]