from django.http import HttpResponse
from django.template import loader

def inicio(request):
    template1 = loader.get_template('index.html')
    render1=template1.render()
    
    return HttpResponse(f'{render1}')