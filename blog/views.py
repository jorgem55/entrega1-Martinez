from dataclasses import fields
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from datetime import datetime
from .forms import SearchMember, SearchPost, FormMember
from .models import Members,Posts
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,'index.html')
    
#---------------
#---------FOOT
#---------------
def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

#---------------
#---------MEMBER
#---------------
def members(request):
    name_to_search = request.GET.get('name')
    if name_to_search:
        members = Members.objects.filter(name__icontains=name_to_search)
    else:
        members = Members.objects.all()
    form = SearchMember()
    return render(request, 'members/members.html', {'members': members, 'form': form})

@login_required
def add_member(request):
    if request.method == 'POST':
        form = FormMember(request.POST)
        
        if form.is_valid():
            data=form.cleaned_data
            date=data.get('buy_date')
            
            member=Members(
                name=data.get('name'),
                bike=data.get('bike'),
                buy_date=date if date else datetime.now()
            )
            member.save()               
            return redirect('members')
        
        else:
            return render (request,'members/add_member.html',{'form':form})
        
    form_member=FormMember()
    
    return render (request,'members/add_member.html',{'form':form_member})

def show_member(request, id):
    members = Members.objects.get(id=id)
    return render(request, 'members/show_member.html', {'member': members})

@login_required
def edit_member(request, id):
    member = Members.objects.get(id=id)
    
    if request.method == 'POST':
        form = FormMember(request.POST)
        if form.is_valid():
            member.name = form.cleaned_data.get('name')
            member.bike = form.cleaned_data.get('bike')
            member.buy_date = form.cleaned_data.get('buy_date')
            member.save()
            
            return redirect('members')
        
        else:
            return render(request, 'members/edit_member.html', {'form': form, 'member': member})
            
    form_member = FormMember(initial={'name': member.name, 'bike': member.bike, 'buy_date': member.buy_date})
    
    return render(request, 'members/edit_member.html', {'form': form_member, 'member': member})

@login_required
def delete_member(request, id):
    members = Members.objects.get(id=id)
    members.delete()
    return redirect('members')

#-------------------------------
#---------POSTS Class Based Views
#-------------------------------
class ListPosts(ListView):
    model=Posts
    template_name = 'posts/posts.html'

    def get_queryset(self):
        title = self.request.GET.get('title', '')
        if title:
            object_list = self.model.objects.filter(title__icontains=title)
        else:
            object_list = self.model.objects.all()
        return object_list
        
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = SearchPost()
        return context
    
class Add_post(LoginRequiredMixin, CreateView):
    model = Posts
    template_name = "posts/add_post.html"
    success_url= '/posts'
    fields=['title','subtitle','content','author','creation_date','image']
    class Meta:
        help_texts = None
    
class Show_post(DetailView):
    model = Posts
    template_name = "posts/show_post.html"
      
class Edit_post(LoginRequiredMixin, UpdateView):
    model = Posts
    template_name = "posts/edit_post.html"
    success_url= '/posts'
    fields=['title','subtitle','content','author','creation_date','image']
    class Meta:
        help_texts = None

class Delete_post(LoginRequiredMixin, DeleteView):
    model = Posts
    template_name = "posts/delete_post.html"
    success_url= '/posts'
