from django.urls import path 
from .views import SimpleUserCreateView
from django.contrib.auth.views import LoginView
# from django.contrib.auth.models import User

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(
        template_name='accounts/login.html', extra_context={'page_title':"Kirish"}), name='login'),
    path('register/', SimpleUserCreateView.as_view(), name='register')
]
