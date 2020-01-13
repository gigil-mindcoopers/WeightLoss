from django.contrib import admin

# Register your models here.
from .models import UserDetails, MyFittness

admin.site.register(UserDetails)
admin.site.register(MyFittness)