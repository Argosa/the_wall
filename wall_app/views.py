from django.shortcuts import render, redirect
from login_reg_app.models import User
from .models import Message, Comment

# Create your views here.
def wall(request):
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'all_messages': Message.objects.all().order_by('-created_at') # the minus in order_by sorts desending order
    }
    return render(request, 'wall.html', context)

def process_post(request):
    postUser = User.objects.get(id=request.session['user_id'])
    postMessage = request.POST['my_post']
    
    print(postUser.first_name, postUser.last_name, postMessage)

    Message.objects.create(message=postMessage, user=postUser)
    print("added to db yo")

    return redirect('wall/')