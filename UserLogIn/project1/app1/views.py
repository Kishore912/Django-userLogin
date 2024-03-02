from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

# Create your views here.
def login(request):
    return render(request,'userlogin.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password1=password1)
        user.save()
        print('user created')
        return redirect('login')
    else:    
        return render(request,'RegisterPage.html')