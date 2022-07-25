from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from datetime import datetime

from .forms import FormMember, SearchMember, SearchPost
from .models import Members,Posts

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

def show_member(request, id):
    members = Members.objects.get(id=id)
    return render(request, 'show_member.html', {'member': members})

def edit_member(request, id):
    member = Members.objects.get(id=id)
    
    if request.method == 'POST':
        form = SearchMember(request.POST)
        if form.is_valid():
            member.name = form.cleaned_data.get('name')
            member.bike = form.cleaned_data.get('bike')
            member.buy_date = form.cleaned_data.get('buy_date')
            member.save()
    
            return redirect('members')
        
        else:
            return render(request, 'member/edit_member.html', {'form': form, 'member': member})
            
    form = SearchMember(initial={'name': member.name, 'bike': member.bike, 'buy_date': member.buy_date})
    
    return render(request, 'member/edit_member.html', {'form': form, 'member': member})

def delete_member(request, id):
    members = Members.objects.get(id=id)
    members.delete()
    return redirect('members')

def posts(request):
    title_to_search = request.GET.get('name')
    
    if title_to_search:
        posts = Posts.objects.filter(name__icontains=title_to_search) 
    else:
        posts = Posts.objects.all()
    
    form = SearchPost()
    return render(request, 'posts.html', {'posts': posts, 'form': form})

def about(request):
    template1 = loader.get_template('about.html')
    render1=template1.render()
    
    return HttpResponse(f'{render1}')

def contact(request):
    template1 = loader.get_template('contact.html')
    render1=template1.render()
    
    return HttpResponse(f'{render1}')
