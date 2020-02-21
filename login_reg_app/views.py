import bcrypt
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
# Create your views here.
def index(request):
    return render(request, 'logincentral.html')

def process_reg(request):
    # make sure the method is post and if not redirect
    if request.method != 'POST':
        return redirect('/')
    
    validator = User.objects.reg_validator(request.POST)
    if not validator['isValid']:
    #if the errors dictionary contains crap, loop through it
        for key, value in validator['errors'].items():
            messages.error(request, value)
        # if errors exist redirect
        return redirect('/')
    else:
        #if there are no errors proceed and retrieve from post
        tempFirstName = request.POST['first_name']
        tempLastName = request.POST['last_name']
        tempEmail = request.POST['email']
        tempPassword = request.POST['password']
        tempHash = bcrypt.hashpw(tempPassword.encode(), bcrypt.gensalt()).decode()
        testVar = f"{tempFirstName} {tempLastName} {tempEmail} {tempPassword} {tempHash}"
        print(testVar)
        new_user = User.objects.create(first_name=tempFirstName, last_name=tempLastName, email=tempEmail, password=tempHash)
        request.session['user_id'] = new_user.id
    return redirect('/success')

def process_login(request):
    if request.method != "POST":
        return redirect('/')
    validator = User.objects.login_validator(request.POST)
    # Check if the errors dictionary contains crap
    if not validator['isValid']:
        for key, value in validator['errors'].items():
            messages.error(request, value)
        # Redirect to login
        return redirect('/')
    else:
        request.session['user_id'] = validator['user_id']
        return redirect('wall/')

def success(request):
    context = {
        'current_user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'success.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')