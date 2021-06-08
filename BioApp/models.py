from django.db import models

class UserManager(models.Manager):
    def validate(self, form):
        errors = {}

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(form['email']):
            errors['email'] = 'Invalid Email Address'

        emailCheck = self.filter(email=form['email'])
        if emailCheck:
            errors['email'] = 'Email Address already in use'
        if len(form['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters'

        if form['password'] != form['confirm']:
            errors['password'] = 'Passwords do not match'

        return errors

class User(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Memory(models.Model):
    image = models.FileField(upload_to='documents/%Y/%m/%d')

class Comment(models.Model): 
    description = models.TextField()
    comment_created = models.DateTimeField(auto_now_add=True)
    comment_updated = models.DateTimeField(add_now=True)