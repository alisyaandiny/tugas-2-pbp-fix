from django.shortcuts import render
from todolist.models import TaskItem
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from datetime import date, datetime
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = TaskItem.objects.filter(user=request.user)
    context = {
        'todolist_data': data_todolist,
        'userName': request.user,
        # 'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account successfully created')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            response.set_cookie('last_login', str(datetime.now()))
            return response
        else:
            messages.info(request, 'Wrong Username or Password!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def create_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        create_task = TaskItem(
            user = request.user,
            title = title,
            description = description,
            date = date.today()
        )
        create_task.save()
        return redirect('todolist:show_todolist')
    return render(request, 'create_task.html')

def toggler(request, id):
   task = TaskItem.objects.get(id = id)
   task.is_finished = not(task.is_finished)
   task.save()
   return redirect('todolist:show_todolist')

def delete_task(request, id):
    task = TaskItem.objects.get(id = id)
    task.delete()
    return redirect('todolist:show_todolist')