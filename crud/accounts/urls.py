from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logoutMessage/', views.LogoutMessageView.as_view(), name='logoutMessage'),
    path('signup/', views.SignUpView.as_view(), name='signup')
]