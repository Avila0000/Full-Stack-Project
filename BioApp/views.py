from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    pass

def memories(request):
    pass

# allows user to add memory and comments
def memoryForm(request):
    pass
# if user not in session redirect to login

# hidden route to add a memory picture
def createMemories(request):
    pass

def commentForm(request, memory_id):
    pass

# add a comment to the memory and hidden route
def createComment(request):
    pass

def logReg(request):
    pass

def hiddenLog(request):
    pass

def hiddenReg(request):
    pass