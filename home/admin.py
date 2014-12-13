from django.contrib import admin
from home.models import Job, About

class AboutAdmin(admin.ModelAdmin):

	list_display = ('location', 'description')

admin.site.register(Job)
admin.site.register(About, AboutAdmin)