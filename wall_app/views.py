from django.shortcuts import render, redirect
from login_reg_app.models import User
from .models import Message, Comment

# Create your views here.
def wall(request):
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'all_messages': Message.objects.all().order_by('-created_at'), # the minus in order_by sorts desending order
        'all_comments': Comment.objects.all().order_by('-created_at'),
    }
    return render(request, 'wall.html', context)

def process_post(request):
    postUser = User.objects.get(id=request.session['user_id'])
    postMessage = request.POST['my_post']
    
    print(postUser.first_name, postUser.last_name, postMessage)

    Message.objects.create(message=postMessage, user=postUser)
    print("added to db yo")

    return redirect('wall/')

def process_comment(request):
    commentMessage = Message.objects.get(id=request.POST['my_id'])
    commentUser = User.objects.get(id=request.session['user_id'])
    postComment = request.POST['my_comment']

    print(commentMessage, commentUser, postComment)
    Comment.objects.create(comment=postComment, user=commentUser, message=commentMessage)
    print('added to db yo')

    return redirect('wall/')

def delete_message(request):
    currentMessageID = request.POST['my_id']
    c = Message.objects.get(id=currentMessageID)
    c.delete()
    print('Message Deleted')

    return redirect('wall/')

def logout(request):
    request.session.clear()
    return redirect('/')