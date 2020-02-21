from __future__ import unicode_literals
import re, bcrypt
from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def reg_validator(self, postData):
        validator = {
            'isValid': True,
            'errors': {}
        }

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        # Add key and values to errors dictionaries
        user = self.filter(email=postData['email'])

        if len(postData['first_name']) < 2:
            validator['isValid'] = False
            validator['errors']['first_name'] = 'Your first name must have at least 2 letters.'
        if len(postData['last_name']) < 2:
            validator['isValid'] = False
            validator['errors']['last_name'] = 'Your last name must have at least 2 characters'
        if not EMAIL_REGEX.match(postData['email']):
            validator['isValid'] = False
            validator['errors']['email'] = 'that is not a real email yo'
        if postData['email'] != postData ['confirm_email']:
            validator['isValid'] = False
            validator['errors']['confirm_email'] = 'emails do not match'
        if user:
            validator['isValid'] = False
            validator['errors']['email_exists'] = 'this email already exists'
        if len(postData['password']) < 8:
            validator['isValid'] = False
            validator['errors']['password'] = 'Your password needs to be 8 characters or more'
        if postData['password'] != postData['confirm_password']:
            validator['isValid'] = False
            validator['errors']['confirm_password'] = "Passwords must match"
        return validator
    
    def login_validator(self, postData):
        validator = {
            'isValid': True,
            'user_id': None,
            'errors': {}
        }
        # See if user is in the database
        user = self.filter(email=postData['email'])
        if user:
            logged_user = user[0]
            print(logged_user)
            if not bcrypt.checkpw(postData['password'].encode(), logged_user.password.encode()):
                # if the password fails give them the boot
                validator['isValid'] = False
                validator['errors']['password'] = 'Your password is incorrect!'
                return validator
            else:
                validator['user_id'] = logged_user.id
                return validator
        else:
            validator['isValid'] = False
            validator['errors']['email'] = "Your email was not found"
            return validator

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __repr__(self):
        return f"{self.first_name} {self.last_name} { self.email }"