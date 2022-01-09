from django.shortcuts import render , redirect
from rest_framework.response import Response
from .models import Notes
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login/")
    
    if request.method == 'POST':
        note = Notes()
        note.title = request.POST.get('title')
        note.desc = request.POST.get('desc')
        note.time = datetime.now()
        # print("=========== the value is: ",len(request.FILES['pic']))
        if len(request.FILES) !=0 :
            note.img = request.FILES['pic']

        # note = Notes(title=title,desc=desc,img=pic,time=datetime.today())
        note.save()
        return redirect("/")
    else:
        notes = Notes.objects.all()
        param = {"notes":notes}
        return render(request, 'index.html',param)

def delete(request,id):
    if request.method == "GET":
        # id = nid
        instance = Notes.objects.get(id=id)
        instance.delete()
        return redirect('/')

    return redirect('/')

def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
            # A backend authenticated the credentials
        else:
            # No backend authenticated the credentials
            return redirect("/login/")
    return render(request,'login.html')

def createUser(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username=username,email=email,password=password)
        print(user)
        user.save()
        return redirect("/login/")
    return render(request,'signup.html')


def logout_view(request):
    logout(request)
    return redirect("/login/")
