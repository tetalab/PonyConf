from django.contrib import admin

from proposals.models import Talk, Topic

admin.site.register(Topic)
admin.site.register(Talk)
