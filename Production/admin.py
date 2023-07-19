from django.contrib import admin

# Register your models here.
from .models import Production
# add to admin panel
admin.site.register(Production)