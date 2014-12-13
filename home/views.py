from django.shortcuts import render
from home.models import Job

def index(request):

	job_list = Job.objects.order_by('id')
	jobs = '- '.join([job.name for job in job_list])
	context_dict = {'jobs': jobs}

	return render(request, 'index.html', context_dict)