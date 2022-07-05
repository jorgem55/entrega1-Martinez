from django.http import HttpResponse
from django.template import loader

def index(request):
    template1 = loader.get_template('index.html')
    render1=template1.render()
    
    return HttpResponse(f'{render1}')

def members(request):
    template1 = loader.get_template('members.html')
    render1=template1.render()
    
    return HttpResponse(f'{render1}')

def template(request):
    template1 = loader.get_template('template.html')
    render1=template1.render()
    
    return HttpResponse(f'{render1}')