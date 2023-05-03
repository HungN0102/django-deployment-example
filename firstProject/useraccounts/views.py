from django.shortcuts import render
from useraccounts.forms import UserForm, UserProfileInfoForm

# for logging in, out
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse 
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    my_dict = {}
    return render(request, 'useraccounts/index.html', context=my_dict)

def register(request):
    registered = False 
    
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user 
            
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            
            registered = True 
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
        
    return render(request, 'useraccounts/registration.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
    })

@login_required
def special(request):
    return HttpResponse('You are logged in, Nice!')

@login_required 
def user_logout(request):
    logout(request)
            
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                login(request, user)
            else:
                return HttpResponse('Account Not Active')
        else:
            print('Someone tried to login and failed!')
            print("Username: {} and password: {}".format(username, password))
            return HttpResponse('Invalid login details supplied')
    else:
        return render(request, 'useraccounts/login.html', context={})