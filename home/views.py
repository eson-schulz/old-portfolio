from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from home.models import Job, About, Github, Project, Resume, Skill
from home.forms import ContactForm
import math

def index(request):
	context_dict = {}

	# Gets the list of names of jobs
	job_list = Job.objects.order_by('id')
	jobs = ' - '.join([job.name for job in job_list])
	context_dict['jobs'] = jobs

	# Gets the list of names of skills in two columns for formatting
	if(len(Skill.objects.all()) > 0):
		skill_list = Skill.objects.order_by('id')
		middle = int(math.ceil(len(skill_list)/2.0))
		skills_1 = ', '.join([skill.name for skill in skill_list[:middle]])
		skills_2 = ', '.join([skill.name for skill in skill_list[middle:]])
		context_dict['skills_1'] = skills_1
		context_dict['skills_2'] = skills_2

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

	# The Contact Form
	if request.method == 'POST':
		form = ContactForm(request.POST)

		if form.is_valid():
			context_dict['sent_message'] = "Thanks for the email!"

			# Sends an email
			subject = "Message from " + form.cleaned_data['name']
			message = form.cleaned_data['message'] + "\n\n" + "-" * 60 + "\nThis was automatically sent from your website"
			sender = form.cleaned_data['email']

			recipients = [settings.USER_EMAIL]

			send_mail(subject, message, sender, recipients)

	else:
		form = ContactForm()
	context_dict['form'] = form

	return render(request, 'index.html', context_dict)