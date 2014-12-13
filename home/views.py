from django.shortcuts import render
from home.models import Job, About  

def index(request):
	context_dict = {}

	job_list = Job.objects.order_by('id')
	jobs = '- '.join([job.name for job in job_list])
	context_dict['jobs'] = jobs

	abouts = About.objects.order_by('id')
	paragraphs = [about.description for about in abouts]
	context_dict['about'] = paragraphs

	return render(request, 'index.html', context_dict)