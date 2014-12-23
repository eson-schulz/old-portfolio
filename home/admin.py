from django.contrib import admin
from home.models import Job, About, Project

class AboutAdmin(admin.ModelAdmin):

	list_display = ('location', 'description')

class ProjectAdmin(admin.ModelAdmin):

	list_display = ('name', 'description', 'date')

admin.site.register(Job)
admin.site.register(About, AboutAdmin)
admin.site.register(Project, ProjectAdmin)