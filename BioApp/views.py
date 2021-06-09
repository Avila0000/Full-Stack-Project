from django.shortcuts import render, redirect
import bcrypt
from .models import *
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def memories(request):
    return render(request, 'memories.html')

# allows user to add memory and comments
def memoryForm(request):
    pass
# if user not in session redirect to login
# its own form html

# hidden route to add a memory picture and will be memory class in models
def createMemories(request):
    pass

# have a many to many field, will be the comment class in models
def commentForm(request, memory_id):
    pass
# its own form html

# add a comment to the memory and hidden route
def createComment(request):
    pass

# will be the user class in models
def logReg(request):
    return render(request, 'login.html')

def hiddenLog(request):
    user = User.objects.filter(email = request.POST['email'])
    if user:
        userLogin = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), userLogin.password.encode()):
            request.session['user_id'] = userLogin.id
            return redirect('/memories/')
        messages.error(request, 'Invalid Credentials')
        return redirect('/')
    messages.error(request, 'That Email is not in our system, please register for an account')
    return redirect('/')

def hiddenReg(request):
    errors = User.objects.validate(request.POST)
    if errors:
        for err in errors.values():
            messages.error(request, err)
        return redirect('/')
    hashedPw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    newUser = User.objects.create(
        full_name = request.POST['full_name'],
        email = request.POST['email'],
        password = hashedPw
    )
    request.session['user_id'] = newUser.id
    return redirect('/memories/')