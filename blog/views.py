from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from datetime import datetime

from .forms import FormMember, SearchMember
from .models import Members

def index(request):
    template1 = loader.get_template('index.html')
    render1=template1.render()
    
    return HttpResponse(f'{render1}')

def members(request):
    name_to_search = request.GET.get('name')
    
    if name_to_search:
        members = Members.objects.filter(name__icontains=name_to_search) 
    else:
        members = Members.objects.all()
    
    form = SearchMember()
    return render(request, 'members.html', {'members': members, 'form': form})
    
def add_member(request):
    if request.method == 'POST':
        form = FormMember(request.POST)
        
        if form.is_valid():
            data=form.cleaned_data
            
            date=data.get('buy_date')
            member=Members(
                name=data.get('name'),
                bike=data.get('bike'),
                buy_date=date if date else datetime.now
            )
            member.save()
        
            return redirect('members')
        else:
            return render (request,'add_member.html',{'form':form})    

    form_member=FormMember()

    return render (request,'add_member.html',{'form':form_member})

def about(request):
    template1 = loader.get_template('about.html')
    render1=template1.render()
    
    return HttpResponse(f'{render1}')

def contact(request):
    template1 = loader.get_template('contact.html')
    render1=template1.render()
    
    return HttpResponse(f'{render1}')
