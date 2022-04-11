from gc import get_objects
from multiprocessing import get_context
from re import template
import django
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from stories.forms import Contact
from .models import Stories

# Create your views here.

# def index(request):
#     return render(request=request, template_name="index.html")

class Index(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['forms'] = Stories.objects.all()
        return context

class Test(ListView):
    model = Stories
    template_name = 'test.html'
    context_object_name = 'forms'

def contact(request):
    if request.method == 'POST':
        print(request.POST.get('name'))
    
    context = {
        'forms':Contact()
    }
    return render(request=request, template_name='contact.html', context=context)

def strories(request):
    context = {
        'stories':Stories.objects.all()
    }
    return render(request, 'strories.html', context)


def single(request, slug):
    context = {
        'forms': Stories.objects.get(slug = slug)
    }
    print('=========>', context)
    return render(request, template_name='single.html', context=context)