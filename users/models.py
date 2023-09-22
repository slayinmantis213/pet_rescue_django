from django.db import models

import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
import random

class UserManager(models.Manager):

    def login_validator(self, data):
        errors = {}
        is_valid = True
        email = data['email']
        pw = data['password']

        if len(email) < 5:
            errors['login'] = "Invalid Email or Password"
            is_valid = False

        if len(pw) < 5 and is_valid == True:
            errors['login'] = "Invalid Email or Password"

            is_valid = False

        if re.search('[A-Z]',pw) is None and is_valid == True:
            errors['login'] = "Invalid Email or Password"
            is_valid = False 
        
        if re.search('[0-9]',pw) is None and is_valid == True:
            errors['login'] = "Invalid Email or Password"
            is_valid = False 
        
        if re.search('[$&!@]',pw) is None and is_valid == True:
            errors['login'] = "Invalid Email or Password" 
            is_valid = False
        
        if is_valid:
            user_in_db = User.objects.filter(email = email)
            if len(user_in_db) < 1:
                errors['login'] = "Invalid Email or Password"
            else:
                user = user_in_db[0]
                if not bcrypt.checkpw(pw.encode(), user.password.encode()):
                    errors['login'] = "Invalid Email or Password"
        
        return errors

    def registration_validator(self, post_data):
        errors = {}
        is_valid = True
        pw = post_data['password']
        con = post_data['pw_confirm']

        if re.search('[A-Z]',pw) is None:
            errors['password'] = "Password must have a number, a capital letter, and a special character($,&,!, @)"  
            is_valid = False 
        
        if re.search('[0-9]',pw) is None:
            errors['password'] ="Password must have a number, a capital letter, and a special character($,&,!, @)"  
            is_valid = False 
        
        if re.search('[$&!@]',pw) is None:
            errors['password'] ="Password must have a number, a capital letter, and a special character ($,&,!, @)" 
            is_valid = False
        
        if len(pw) < 8:
            errors['password'] = "Passwords must be at least eight characters in length."
            is_valid = False

        if len(pw) > 85:
            errors['password'] = "Passwords must be under 85 characters in length."
            is_valid = False

        if pw != con:
            errors['password'] ="Password and confirmation must match." 
            is_valid = False

        if len(post_data['username']) < 1:
            errors['username'] ="Please provide a username."
            is_valid = False

        if len(post_data['username']) > 45:
            errors['username'] = "Username must be under 45 characters in length."
            is_valid = False

        if len(post_data['email']) > 45:
            errors['email'] = "Email must be under 45 characters in length.", "reg"
            is_valid = False

        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = "Email invalid."
            is_valid = False
        
        if is_valid:
            c = User.objects.filter(email = post_data['email'])
            if len(c) > 0:
                errors['email'] = "Email already in use."
            else:
                c = User.objects.filter(username = post_data['username'])
                if len(c) > 0:
                    errors['username'] = "Username already in use."

        return errors
        

class User(models.Model):
    username = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=85)
    gifts = models.IntegerField(default=10)
    feathers = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    staticmethod
    def gift(user):
        x = random.randrange(0,4)
        if x == 3:
            return False
        else:
            user.gifts += 1
            user.save()
            return True