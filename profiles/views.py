from django.shortcuts import render,redirect

# Create your views here.

from django.views.generic import ListView

from django.views.generic.edit import UpdateView,CreateView,FormView

from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.forms import PasswordChangeForm

from .models import ads,User




class dashboard(ListView):

    template_name='dashboard.html'

    model=ads

    paginate_by=5



class Edit_Profile(UpdateView):

    template_name="user-profile.html"
       
    model=User

    fields=['username','email','first_name','last_name','phone']

    success_url='/profiles/dashboard'

    def get_queryset(self):
         qs=super().get_queryset()
         return qs.filter(username=self.request.user)

class change_password(PasswordChangeView):
    template_name="index.html"

    form_class=PasswordChangeForm

    success_url='/profiles/dashboard'

    

