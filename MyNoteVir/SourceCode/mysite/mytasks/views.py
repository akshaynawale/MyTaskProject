from django.shortcuts import  HttpResponse
from django.template import loader
from .models import Task, User
# Create your views here.


def index(request):
	print_msg =  {}
	for task in Task.objects.all():
		print_msg[task.title] = str(task.owner)
	template = loader.get_template('mytasks/index.html')
	return HttpResponse(template.render({'task_lines': print_msg}))
