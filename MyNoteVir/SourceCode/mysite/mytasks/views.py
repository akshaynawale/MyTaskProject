from django.shortcuts import  HttpResponse, render
from django.template import loader
from .models import Task, User
from django.template import RequestContext
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
        all_users.append(user.user_name)
    all_users.append('all')
    # print(all_users)
    return render(
            request, 
            'mytasks/index.html',
            {'task_lines': print_msg, 'all_users': all_users, 'selected': owner}
        )

def home_page(request):
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
    return render(
            request,
            'mytasks/create_account_result.html',
            {'result': 
                ('Your account is successfully created. Go to login page '
                 'to login and access the website. Thank you!')
            }
            )
