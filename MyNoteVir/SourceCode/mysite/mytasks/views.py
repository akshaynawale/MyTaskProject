from django.shortcuts import  HttpResponse, render
from django.template import loader
from .models import Task
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# Create your views here.

def index(request, owner='all'):
    print_msg = []
    for task in Task.objects.all():
        if owner == 'all':
            msg = {}
            msg['title'] = task.title
            msg['owner'] = str(task.owner)
            p_date = str(task.pub_date)
            p_date = p_date.split()[0]
            msg['pub_date'] = str(p_date)
            print_msg.append(msg)
        else:
            if str(task.owner) == owner:
                msg = {}
                msg['title'] = task.title
                msg['owner'] = str(task.owner)
                p_date = str(task.pub_date)
                p_date = p_date.split()[0]
                msg['pub_date'] = str(p_date)
                print_msg.append(msg)
    all_users = []
    for user in User.objects.all():
        all_users.append(user.username)
    all_users.append('all')
    # print(all_users)
    return render(
            request, 
            'mytasks/index.html',
            {'task_lines': print_msg, 'all_users': all_users, 'selected': owner}
        )

def home_page(request):
    user_name = request.POST['uname']
    password = request.POST['pwd']
    user = authenticate(username=user_name, password=password)
    if user is not None:
        return index(request, owner=user_name)
    else:
        return render(
                request, 
                'mytasks/login_page.html', 
                {'fail_warning': 'User not found try again'}
            )

def home_page_by_owner(request):
    try:
        req_owner = request.POST['owner']
    except:
        req_owner = 'all'
    return index(request, owner=req_owner)

def login_page(request):
    return render(
            request,
            'mytasks/login_page.html'
            )

def create_account_page(request):
    return render(
            request,
            'mytasks/create_account.html'
            )

def create_account_result_page(request):
    first_name = request.POST['first']
    last_name = request.POST['last']
    email_id = request.POST['email']
    user_name = request.POST['uname']
    password = request.POST['pwd']
    user_obj = User.objects.create_user(
            user_name, 
            email=email_id, 
            password=password)
    user_obj.first_name = first_name
    user_obj.last_name = last_name
    user_obj.save()
    message = ('Your account is successfully created. Go to login page '
               'to login and access the website. Thank you!')
    # except:
    #    message = "Something went wrong. Please try again."
    
    return render(
            request,
            'mytasks/create_account_result.html',
            {'result': message}
            )
