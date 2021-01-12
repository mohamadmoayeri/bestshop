from django.shortcuts import render,redirect

from django.urls import reverse_lazy

# Create your views here.

from django.views.generic import ListView

from django.views.generic.edit import UpdateView,CreateView,FormView

from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView

from django.contrib.auth.forms import PasswordChangeForm

from .models import ads,User




class dashboard(ListView):

    template_name='dashboard.html'

    model=ads

    paginate_by=5



class Edit_Profile(UpdateView):

    template_name="user-profile.html"
       
    model=User

    fields=['avatar','username','email','first_name','last_name','phone']

    success_url='/profiles/dashboard'

    def get_queryset(self):
         qs=super().get_queryset()
         return qs.filter(username=self.request.user)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["person"] = User.objects.get(username=self.request.user)
        return context
    

class change_password(PasswordChangeView):
    template_name="change_password.html"

    form_class=PasswordChangeForm

    success_url=reverse_lazy('change_password_done')

class change_password_done(PasswordChangeView):

    template_name="change_password_done.html"




    

