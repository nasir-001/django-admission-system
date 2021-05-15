from django.contrib import admin
from .models import User, Admitted

# Register your models here.

admin.site.site_header = 'Online Application System'
admin.site.register(User)
admin.site.register(Admitted)