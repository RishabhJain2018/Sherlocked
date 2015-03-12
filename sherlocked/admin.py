from django.contrib import admin
from sherlocked.models import *

admin.site.register(Question)
admin.site.register(UserDetail)

# class AppnameAdmin(admin.ModelAdmin):
#     list_display = ('')

# admin.site.register(Questions,AppnameAdmin)