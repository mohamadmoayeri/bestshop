from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView



class home(TemplateView):

    def get(self,request):

        context={
            
        }

        return render(request,'index.html',context)
