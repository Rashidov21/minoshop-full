from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
# Create your views here.

class SimpleUserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'accounts/login.html'
    success_url = '/'
    extra_context={'page_title':"Ro'yhatdan o'tish"}
    
    def form_valid(self, form):
        # if 'profile' in dir(self.get_object()):
        #     # profile bor 
        # else:
        #     p_obj = Profile.objects.create()
        #     self.object.profile = p_obj
        print(dir(self))
        print(dir(form))
        # form = self.form 
        return super().form_valid(form)
    