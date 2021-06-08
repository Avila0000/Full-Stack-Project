from django.shortcuts import render, redirect

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

# hidden route to add a memory picture and will be memory class in models
def createMemories(request):
    pass

# have a many to many field, will be the comment class in models
def commentForm(request, memory_id):
    pass

# add a comment to the memory and hidden route
def createComment(request):
    pass

# will be the user class in models
def logReg(request):
    pass

def hiddenLog(request):
    pass

def hiddenReg(request):
    pass