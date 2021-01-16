from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView,ListView

from profiles.models import User,ads



class home(TemplateView):

    def get(self,request):

        context={
            
        }

        return render(request,'index.html',context)


class categories(ListView):

    template_name='category.html'

    model=ads

    def get_queryset(self):
        qs=super().get_queryset()
        category=self.kwargs['category']

        return qs.filter(category=category)
    