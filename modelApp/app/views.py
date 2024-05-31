from django.shortcuts import render,redirect
from .models import Member

# Create your views here.
def index(request):
    members=Member.objects.all()
    return render(request,'index.html',{'members':members})

def add(request):
    return render(request,'add.html')

def register_member(request):
    first=request.POST['first']
    second=request.POST['second']
    country=request.POST['country']
    member=Member(firstname=first,secondname=second,country=country)
    member.save()
    return redirect('/')

def delete_member(request,id):
    member=Member.objects.get(id=id)
    member.delete()
    return redirect('/')

def get_member(request,id):
    member=Member.objects.get(id=id)
    return render(request,'update.html',{"member":member})

def update_member(request,id):
    first=request.POST['first']
    second=request.POST['second']
    country=request.POST['country']
    member=Member.objects.get(id=id)
    member.firstname=first
    member.secondname=second
    member.country=country
    member.save()
    return redirect('/')


    return render(request,'update.html',{"member":member})