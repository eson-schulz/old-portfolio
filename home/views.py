from django.shortcuts import render
from home.models import Job, About, Github, Project, Resume

def index(request):
	context_dict = {}

	# Gets the list of names of jobs
	job_list = Job.objects.order_by('id')
	jobs = ' - '.join([job.name for job in job_list])
	context_dict['jobs'] = jobs

	# Gets the item that's the first paragraph, second paragraph, etc
	name = ('first_paragraph', 'second_paragraph', 'footer_paragraph')
	for x in range(0, 3):
		try:
			context_dict[name[x]] = About.objects.get(location=str(x + 1)).description
		except(About.DoesNotExist):
			context_dict[name[x]] = "Error: " + name[x] + " does not exist."

	# Gets the projects in a list from newest to oldest
	context_dict['projects'] = Project.objects.order_by('-date')

	# Gets the single resume
	if(len(Resume.objects.all()) > 0):
		context_dict['resume'] = Resume.objects.all()[0]

	# Gets the single Github Model
	if(len(Github.objects.all()) > 0):
		context_dict['github'] = Github.objects.all()[0]

	return render(request, 'index.html', context_dict)