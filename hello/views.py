# from django.template import loader
from django.http import HttpResponse
from django.template import loader
from .models import Hello

def hello(request):
    mymembers = Hello.objects.all().values()
    template = loader.get_template('all.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Hello.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    mymembers = Hello.objects.all().values()
    template = loader.get_template('template.html')
    context = {
        # 'firstname': 'Gaus'
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))