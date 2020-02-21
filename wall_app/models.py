from django.db import models
from login_reg_app.models import User

# Create your models here.
class Message(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User, related_name='user_messages', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"{message} {user.first_name} {user.last_name} {created_at}"

class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, related_name='user_comments', on_delete = models.CASCADE)
    message = models.ForeignKey(Message, related_name='message_comments', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"{comment} {user.first_name} {user.last_name}"
